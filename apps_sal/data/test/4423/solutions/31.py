N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    p = int(p)
    SP.append((s, p, i + 1))

SP.sort(key=lambda x: (x[0], -x[1]))
for i in range(N):
    print((SP[i][2]))
