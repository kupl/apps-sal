n = int(input())
flg = [0]*100000
for _ in range(n):
    l,r = list(map(int,input().split()))
    for i in range(l,r+1):
        flg[i-1] = 1
print((flg.count(1)))

