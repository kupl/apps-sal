k = int(input())
if 7 % k == 0:
    print(1)
else:
    a = []
    a.append(7 % k)
    t = 0
    for i in range(2, k + 1):
        x = (10 * a[i - 2] + 7) % k
        if x == 0:
            print(i)
            break
        else:
            a.append(x)
            t += 1
    if t == k - 1:
        print(-1)
