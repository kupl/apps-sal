n = int(input())
for i in range(n):
    a = int(input())
    b = max(len(str(a)) * 9 - 9, 0)
    j = '1' * len(str(a))
    j = int(j)
    t = j
    for q in range(9):
        if t <= a:
            t += j
            b += 1
    print(b)
