N, K = list(map(int,input().split()))
D = set(input().split())

for k in range(N,10**9):
    f = 1
    for e in str(k):
        if e in D:
            f = 0
            break
    if f == 1:
        print(k)
        return

