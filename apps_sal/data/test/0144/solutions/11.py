n = int(input())

s = input()

maxi = -1

for x in range(901):
    f = False
    acc = 0
    cnt = 0
    for y in range(n):
        if acc + int(s[y]) > x:
            f = True
            break
        elif acc + int(s[y]) == x:
            acc = 0
            cnt += 1
        else:
            acc += int(s[y])
    if f:
        continue
    elif acc == 0 and cnt >= 2:
        maxi = x

if maxi == -1:
    print("NO")
else:
    print("YES")
