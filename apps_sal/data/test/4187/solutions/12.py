n = int(input())
ai = list(map(int,input().split()))
num = 0
num2 = 0
for i in range(n):
    if ai[i] == 0:
        break
    num += 1
for i in range(n-1,-1,-1):
    if ai[i] == 0:
        break
    num2 += 1
ans = num + num2
num3 = 0
for i in range(n):
    if ai[i] == 0:
        num3 = 0
    else:
        num3 += 1
        ans = max(ans,num3)
print(ans)
        

