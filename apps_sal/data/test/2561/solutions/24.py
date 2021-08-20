n = int(input())
for i in range(n):
    x = int(input())
    ans = 1
    for j in range(33):
        if 1 << j & x:
            ans *= 2
    print(ans)
