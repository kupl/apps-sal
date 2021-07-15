n = int(input())
M = [int(s) for s in input().split()]
R = [int(s) for s in input().split()]
c = 0
for i in range(100000):
    bool = False
    for j in range(n):
        if i % M[j] == R[j]:
            bool = True
            break
    if bool:
        c += 1
print(c/100000)
