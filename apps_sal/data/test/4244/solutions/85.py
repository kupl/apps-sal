N = int(input())
X = list(map(int, input().split()))
ans = 10 ** 6
for i in range(1, 101):
    tem = 0
    for j in range(N):
        tem += (X[j] - i) ** 2
    if tem <= ans:
        ans = tem
print(ans)
