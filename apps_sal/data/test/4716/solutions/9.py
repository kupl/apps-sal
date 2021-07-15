# スペース区切りの整数の入力
n, k = map(int, input().split())
# スペース区切りの整数の入力
data =  list(map(int, input().split()))
l = sorted(data, reverse=True)
ans = 0

for i in range(k):
    ans += l[i]

print(ans)
