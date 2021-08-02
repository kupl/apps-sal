s = int(input())
a = [s]
ans = 0
for i in range(1000000):
    if a[i] % 2 == 0:
        if a[i] / 2 in a:
            ans = i + 2
            break
        a.append(a[i] / 2)
    else:
        if 3 * a[i] + 1 in a:
            ans = i + 2
            break
        a.append(3 * a[i] + 1)
print(ans)
