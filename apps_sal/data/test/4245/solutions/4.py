a,b = list(map(int,input().split()))
plug = 1
cnt = 0
while plug < b :
    plug = plug+a-1
    cnt += 1
print(cnt)

