(n, k) = list(map(int, input().split()))
t = input()
a = -1
for i in range(1, n + 1):
    if t.startswith(t[i:]):
        a = i
        break
pre = t[:a]
ans = pre * (k - 1) + t
print(ans)
