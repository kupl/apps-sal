n = int(input())
a = list(map(int, input().split()))
ans = [0] * (n + 1)
for x in a:
    ans[x] += 1
for i in range(1, n + 1, 1):
    print(ans[i])
