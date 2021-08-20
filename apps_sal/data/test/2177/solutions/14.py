q = int(input())
for ew in range(q):
    (a, b) = map(int, input().split())
    p = 0
    pi = 0
    while True:
        if p * 10 + 9 <= b:
            p = p * 10 + 9
            pi += 1
        else:
            break
    print(a * pi)
