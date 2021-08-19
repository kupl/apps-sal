# B Digital Gifts
N = int(input())
X = [list(map(str, input().split())) for _ in range(N)]
gifts = 0
for i in range(N):
    if X[i][1] == 'JPY':
        gifts += int(X[i][0])
    else:
        gifts += float(X[i][0]) * 380000
print(gifts)
