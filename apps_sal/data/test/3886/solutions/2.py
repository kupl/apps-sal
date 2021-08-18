s = "What are you doing at the end of the world? Are you busy? Will you save us?"


def L(n):
    return 143 * 2**n - 68 if n < 55 else 10**18


beg = 'What are you doing while sending "'
mid = '"? Are you busy? Will you send "'
end = '"?'
beglen = len(beg)
midlen = len(mid)
endlen = len(end)


def f(n, k):
    while True:
        if n == 0:
            if k < len(s):
                return s[k]
            return '.'
        n -= 1

        if k < beglen:
            return beg[k]
        k -= beglen
        if k < L(n):
            continue
        k -= L(n)
        if k < midlen:
            return mid[k]
        k -= midlen
        if k < L(n):
            continue
        k -= L(n)
        if k < endlen:
            return end[k]
        return '.'


q = int(input())

ans = []
for _ in range(q):
    n, k = list(map(int, input().split()))
    k -= 1
    ans.append(f(n, k))
print(''.join(ans))
