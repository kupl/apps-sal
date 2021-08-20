n = int(input())
L = []
for i in range(n):
    (s, p) = input().split()
    L.append([s, -int(p), i + 1])
L.sort()
for i in range(n):
    print(L[i][2])
