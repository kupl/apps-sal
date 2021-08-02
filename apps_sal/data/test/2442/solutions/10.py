t = int(input())

for i in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    m1, m2 = 0, 0
    for i in range(101):
        if k.count(i) < 2:
            m1 = i
            break
    for i in range(m1, 101):
        if k.count(i) < 1:
            m2 = i
            break
    print(m1 + m2)
