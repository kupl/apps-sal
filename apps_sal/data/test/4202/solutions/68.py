#50 C - Remainder Minimization 2019 AC (hint)
L,R = map(int,input().split())

ans = 2020
# O(2019*2019)
# i は 2019 個以下
for i in range(L,R+1):
    # j は　2019 個以下
    for j in range(i+1,R+1):
        n = i*j
        if n%2019 == 0:
            ans = 0
            break
        n = n%2019
        ans = min(ans,n)
    else:
        continue
    break
print(ans)
