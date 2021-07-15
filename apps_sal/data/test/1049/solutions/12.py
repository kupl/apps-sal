n,d = list(map(int,input().split()))
ans = 0
temp = 0
for i in range(d):
    ai = input()
    temp2 = 0
    for j in ai:
        if j == "0":
            temp += 1
            temp2 = 1
            break
    if temp2 == 0:
        temp = 0
    if temp > ans:
        ans = temp
print(ans)
    

