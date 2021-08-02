n = int(input())
bef = 0
mn = 0
flg = 0
H = list(map(int, input().split()))
#H=[int(input()) for i in range(n)]
# print(H)
for i in range(n):
    h = H[i]
    if h < mn:
        flg = 1
    mn = max(mn, h - 1)

if(flg == 1):
    print("No")
else:
    print("Yes")
