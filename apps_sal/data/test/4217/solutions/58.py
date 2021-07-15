n, m = map(int, input().split())

ans = [0] * m

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if j == 0:
            pass
        else:
            ans[tmp[j] - 1] += 1
print(ans.count(n))
