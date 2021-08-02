def solve(n, k, l):
    ki = i = s = 0; po = 1
    for j in range(n):
        s += (l[j] == 0)
        while s > k: s -= (l[i] == 0); i += 1
        if j - i > ki - po: po, ki = i, j
    return ki - po + 1


n, k = map(int, input().split())
s = input()
a1, a2 = [], []
for i in range(n):
    if s[i] == 'a':
        a1.append(1)
        a2.append(0)
    else:
        a1.append(0)
        a2.append(1)
print(max(solve(n, k, a1), solve(n, k, a2)))
