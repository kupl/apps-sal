L = list(map(int,input().split()))
Ans = 0
for i in range(4):
    if L[i] == sum(L) - L[i]:
        Ans += 1 

for j in range(1,4):
    if L[0] + L[j] == sum(L) - L[0] - L[j]:
        Ans += 1
if Ans != 0:
    print("Yes")
else:
    print("No")


