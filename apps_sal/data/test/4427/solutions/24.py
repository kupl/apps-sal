(r, D, x2000) = map(int, input().split())
ans = [x2000]
for i in range(10):
    ans.append(r * ans[i] - D)
for h in range(1, 11):
    print(ans[h])
