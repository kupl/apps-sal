N, K = map(int, input().split())
S = set(input().split())
while True:
    L = list(str(N))
    for i in L:
        if i in S:
            break
    else:
        break
    N += 1
print(N)
