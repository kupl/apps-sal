v = int(input())
a = list(map(int, input().split()))
i = 0
for j in range(1, 9):
    if a[j] <= a[i]:
        i = j
if v // a[i] == 0:
    print(-1)
else:
    length = v // a[i]
    b = (v // a[i]) * a[i]
    ans = []
    while v >= b:
        j = 8
        while j > i:
            if v >= b + a[j] - a[i]:
                break
            j -= 1
        if j == i:
            break
        b += a[j] - a[i]
        ans += [j + 1]
    print(''.join(map(str, ans + [i + 1] * (length - len(ans)))))
