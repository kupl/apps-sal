def check(M):
    sm = 0
    for i in range(n):
        if a[i] > M:
            sm += b[i]
    return sm <= M


gans = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    L = 0
    R = max(a)
    while R - L > 1:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M
    gans.append(R)
print(*gans, sep='\n')

