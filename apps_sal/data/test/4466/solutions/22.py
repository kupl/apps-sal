x, y, z = map(int,input().split())

cnt = 1
x -= y + 2*z

while x >= y + z:
    cnt += 1
    x -= y + z
print(cnt)
