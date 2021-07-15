qq = int(input())
for _ in range(qq):
    n = int(input())
    dat = list(map(int, input().split()))
    if n == 1:
        print("YES")
        continue
    c = dat[0] % 2
    f = True
    for i in range(n):
        if c != dat[i] % 2:
            f = False
    print("YES" if f else "NO")

