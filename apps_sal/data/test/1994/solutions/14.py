from itertools import accumulate


def zfunc(s):
    n = len(s)
    z = [0] * n
    left = right = 0
    for i in range(1, n):
        if i <= right:
            z[i] = min(z[i - left], right - i + 1)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z


s = input()
ans = set()
z = zfunc(s)
z[0] = len(s)
res = [0] * (len(s) + 1)

for i in z:
    res[i] += 1

res = [*accumulate(res[::-1])][::-1]

for i, j in enumerate(z[::-1]):
    if j > i:
        ans.add((j, res[j]))
print(len(ans))
for i in sorted([*ans]):
    print(*i)
