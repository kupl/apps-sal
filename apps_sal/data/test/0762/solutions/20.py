n,b = list(map(int,input().split()))
ai = list(map(int,input().split()))
ai2 = [0] * n
temp1 = 0
for i in range(n-1):
    if ai[i] % 2 == 0:
        temp1 += 2
    if temp1 == i + 1:
        ai2[i] = 1
        
ai4 = []

temp1 = 0
for i in range(n-1,0,-1):
    if ai[i] % 2 == 0:
        temp1 += 2
    if temp1 == n - i:
        if ai2[i-1] == 1:
            ai4 += [abs(ai[i] - ai[i-1])]
ai4.sort()
ans = 0
i = 0
while  i < len(ai4) and b >= ai4[i]:
    b -= ai4[i]
    ans += 1
    i += 1
print(ans)

