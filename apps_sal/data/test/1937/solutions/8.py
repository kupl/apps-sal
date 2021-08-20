n = int(input())
s = [int(i) for i in input().split()]
t = [0] * n
t[-1] = s[0]
for i in range(1, n // 2):
    if t[n - i] < s[i] - t[i - 1]:
        (t[i], t[n - 1 - i]) = (s[i] - t[n - i], t[n - i])
    else:
        (t[i], t[n - 1 - i]) = (t[i - 1], s[i] - t[i - 1])
print(*t)
