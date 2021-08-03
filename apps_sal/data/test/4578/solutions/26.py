N, X = map(int, input().split())
minN = 10**5
for i in range(N):
    crt = int(input())
    if minN > crt:
        minN = crt
    X -= crt
print(N + X // minN)
