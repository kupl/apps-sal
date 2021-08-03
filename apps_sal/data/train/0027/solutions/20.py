t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for j in range(0, n):
        if a[j] % 2 == 0:
            num = 0
            k = a[j]
            while k % 2 == 0:
                k //= 2
                num += 1
            b.append([k, num])
    b.sort()
    ans = 0
    length = len(b)
    for q in range(0, length - 1):
        if b[q][0] != b[q + 1][0]:
            ans += b[q][1]
    if length != 0:
        print(ans + b[length - 1][1])
    else:
        print(ans)
