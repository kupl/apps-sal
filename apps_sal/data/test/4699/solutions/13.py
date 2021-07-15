N, K = map(int, input().split())
D = list(input().split())

while True:
    n = str(N)
    for i in range(K):
        f = 0
        if D[i] in n:
            N += 1
            f = 1
            break
    if f == 0:
        break

print(N)
