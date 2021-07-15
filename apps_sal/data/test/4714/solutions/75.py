a,b=map(int,input().split())
cnt = 0
for i in range(a,b+1):
    i = str(i)
    if i == i[::-1]:
        cnt +=1
print(cnt)
