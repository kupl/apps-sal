a, b, f, k = map(int, input().split())
im = False
fuel = b
cnt = 0
for i in range(k):
    if(i % 2 == 0):
        if(fuel - f < 0):
            im = True
            break
        if(i < k - 1):
            if(fuel - (2 * a - f) < 0):
                cnt += 1
                fuel = b - (a - f)
            else:
                fuel -= a
        else:
            if(fuel - a < 0):
                cnt += 1
                fuel = b - (a - f)
            else:
                fuel -= a
    else:
        if(fuel - (a - f) < 0):
            im = True
            break
        if(i < k - 1):
            if(fuel - (a + f) < 0):
                cnt += 1
                fuel = b - f
            else:
                fuel -= a
        else:
            if(fuel - a < 0):
                cnt += 1
                fuel = b - f
            else:
                fuel -= a
    if(fuel < 0):
        im = True
        break

print(-1 if im else cnt)
