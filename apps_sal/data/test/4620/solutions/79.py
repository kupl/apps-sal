n = int(input())
ans = [0] * n

for i in range(1, n):
    c, s, f = list(map(int, input().split()))

    for j in range(i):
        ans[j] = max(ans[j], s)
        ans[j] = ((ans[j]+f-1)//f) * f
        ans[j] += c

for a in ans:
    print(a)
