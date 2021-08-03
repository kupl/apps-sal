t = int(input())
for wefe in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    k = list(map(int, input().split()))
    parl = 0
    park = 0
    for i in l:
        if i % 2 == 0:
            parl += 1
    for i in k:
        if i % 2 == 0:
            park += 1
    print(parl * park + (n - parl) * (m - park))
