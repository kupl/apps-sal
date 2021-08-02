t = int(input())
for test in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    m = int(input())
    b = list(map(int, input().split(" ")))
    odda = 0
    evena = 0
    oddb = 0
    evenb = 0
    res = 0
    for i in range(n):
        if a[i] % 2 == 0:
            evena += 1
        else:
            odda += 1
    for i in range(m):
        if b[i] % 2 == 0:
            evenb += 1
        else:
            oddb += 1
    res += (evena * evenb)
    res += (odda * oddb)
    print(res)
