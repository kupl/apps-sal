s = int(input())
a = [s]
for i in range(1, 1000001):
    if a[i - 1] % 2 == 0:
        x = a[i - 1] // 2
        if x in a:
            print(i + 1)
            break
        else:
            a.append(x)
    else:
        y = a[i - 1] * 3 + 1
        if y in a:
            print(i + 1)
            break
        else:
            a.append(y)
