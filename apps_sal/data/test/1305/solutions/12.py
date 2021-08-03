n = int(input())
a = list(map(int, input().split()))
t25, t50, t100, c = 0, 0, 0, 1
for ele in a:
    if ele == 25:
        t25 += 1
    elif ele == 50:
        if t25:
            t50 += 1
            t25 -= 1
        else:
            c = 0
            break
    elif ele == 100:
        if t50 and t25:
            t100 += 1
            t25 -= 1
            t50 -= 1
        elif t25 >= 3:
            t100 += 1
            t25 -= 3
        else:
            c = 0
            break
if c:
    print("YES")
else:
    print("NO")
