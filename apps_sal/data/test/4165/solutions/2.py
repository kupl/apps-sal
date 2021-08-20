N = int(input())
l = list(map(int, input().split()))
sum = 0
flg = True
for i in range(N):
    sum = sum + l[i]
for j in range(N):
    if sum - l[j] <= l[j]:
        flg = False
        break
if flg == True:
    print('Yes')
else:
    print('No')
