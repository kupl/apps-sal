def get_longest_palindromes(strng):
    N = len(strng)
    cache = [[None] * N for _ in range(N)]

    def is_palindrome(lo, hi):
        if cache[lo][hi] is not None:
            return cache[lo][hi]

        if lo == hi:
            return True
        elif lo + 1 == hi:
            return strng[lo] == strng[hi]

        ans = False if strng[lo] != strng[hi] else is_palindrome(lo+1, hi-1)
        cache[lo][hi] = ans
        return ans

    def generate_palindromes():
        ret = []
        longest = N
        found = False

        if not strng:
            return ['']

        for l in range(N, 0, -1):
            found = False
            for s in range(N-l+1):
                if is_palindrome(s, s+l-1):
                    found = True
                    ret.append(strng[s:s+l])
            if found:
                break
        return ret

    return generate_palindromes()
try:
    n = int(input())
    string = input()
    print(len(get_longest_palindromes(string)[0]))
    print(get_longest_palindromes(string)[0])
except:
    pass
