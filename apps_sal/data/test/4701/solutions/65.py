N = int(input())
K = int(input())


C = 1
for i in range(N):
    if C * 2 > C + K:
        C = C + K
    else:
        C = C * 2

print(C)
