N = int(input())
(D, X) = map(int, input().split())
choco = 0
for i in range(N):
    A = int(input())
    choco += 1
    for j in range(1, 100):
        if A * j + 1 <= D:
            choco += 1
        else:
            break
print(choco + X)
