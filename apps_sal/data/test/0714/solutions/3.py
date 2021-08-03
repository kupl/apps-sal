n = int(input())
s = [int(i) for i in input().split()]
t = []
for i in range(n):
    t.append((s[i], i + 1))
r = (sum(s) // (n // 2))
t.sort()
for i in range(n // 2):
    print(t[i][1], t[n - i - 1][1])
