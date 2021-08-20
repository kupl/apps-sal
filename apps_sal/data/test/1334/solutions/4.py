def solve(k, s):
    letters = sorted(set(list(s)))
    res = [0] * k
    if k > len(s):
        return s + letters[0] * (k - len(s))
    largest_letter = letters[-1]
    i = k - 1
    while s[i] == largest_letter:
        res[i] = letters[0]
        i -= 1
    ind = letters.index(s[i])
    res[i] = letters[ind + 1]
    for j in range(i - 1, -1, -1):
        res[j] = s[j]
    return ''.join(res)


(n, k) = map(int, input().split())
s = input().strip()
print(solve(k, s))
