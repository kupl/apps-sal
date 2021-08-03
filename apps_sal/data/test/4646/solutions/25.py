n = int(input())

for _ in range(n):
    input()
    a = list(map(int, input().split()))
    c_e, c_n = 0, 0
    for i, x in enumerate(a):
        if i % 2 == 0 and x % 2 == 1:
            c_e += 1
        if i % 2 == 1 and x % 2 == 0:
            c_n += 1
    if c_e != c_n:
        print(-1)
    else:
        print(c_e)
