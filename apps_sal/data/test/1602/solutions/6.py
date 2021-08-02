n = int(input())
a = list(map(int, input().split()))

for d in range(29, -1, -1):
    bit = 1 << d
    count, j = 0, 0
    for i, x in enumerate(a):
        if bit & x:
            count += 1
            if count == 2:
                break
            else:
                j = i
    if count == 1:
        print(a[j], *(a[:j] + a[j + 1:]))
        break
else:
    print(*a)
