for f in range(int(input())):
    n = int(input())
    m = n // 2
    prev = 1
    cur = 3
    mov = 0
    for i in range(m):
        mov += (i + 1) * (cur**2 - prev**2)
        prev += 2
        cur += 2
    print(mov)
