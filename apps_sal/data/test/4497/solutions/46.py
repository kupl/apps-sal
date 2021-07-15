n = int(input())
num = [i for i in range(1,n+1)]
jou = [2**j for j in range(0,7)]
for l in jou:
    if l in num:
        ans = l
    else:
        break
print(ans)
