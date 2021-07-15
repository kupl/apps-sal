l = int(input())
y = int(input())
g = int(input())
cnt = 0
while l >= 1 and y>=2 and g >=4:
    cnt+=7
    l-=1
    y-=2
    g-=4
print(cnt)
