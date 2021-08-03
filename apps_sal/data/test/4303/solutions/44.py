n, k = map(int, input().split())
xlist = list(map(int, input().split()))
ans = 10**20
for i in range(n - k + 1):
    ans = min(abs(xlist[i] - xlist[i + k - 1]) + min(abs(xlist[i]), abs(xlist[i + k - 1])), ans)
print(ans)
