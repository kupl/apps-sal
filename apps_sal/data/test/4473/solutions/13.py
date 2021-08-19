t = int(input())
Q = [list(map(int, input().split())) for i in range(t)]
for (a, b, k) in Q:
    if k % 2 == 0:
        print((a - b) * k // 2)
    else:
        print((a - b) * (k // 2) + a)
