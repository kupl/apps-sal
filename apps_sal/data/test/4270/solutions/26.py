N = int(input())
x = list(map(int, input().split()))
x.sort()
ans = x[0]
for i in range(N - 1):
    ans = (ans + x[i + 1]) / 2
print(ans)
