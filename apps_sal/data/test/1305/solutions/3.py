n = int(input())
a = list(map(int, input().split()))
s = 0
d = 0
for i in a:
    if i == 25:
        s += 1
    if i == 50:
        if s == 0:
            print('NO')
            return
        else:
            s -= 1
            d += 1
    if i == 100:
        if d > 0 and s > 0:
            s -= 1
            d -= 1
        elif s > 2:
            s -= 3
        else:
            print("NO")
            return
print('YES')
