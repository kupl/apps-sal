A, B = map(int,input().split())
ans = 0

for i in range(A, B+1):
    num = str(i)
    #print(i,num[0:2],num[::-1][0:2])
    if num[0:2] == num[::-1][0:2]:
        ans += 1
print(ans)
