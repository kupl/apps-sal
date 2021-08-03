a = int(input())
b = [0 for i in range(1000001)]
q = 0
cnt = 0
mx = 0
for i in range(a):
    z, x = input().split()
    x = int(x)
    if z == '+':
        b[x] = 1
        cnt += 1
    if z == '-':
        if b[x] == 0:
            mx = mx + 1
            cnt += 1
        b[x] = 0
        cnt -= 1
    mx = max(mx, cnt)
print(mx)
