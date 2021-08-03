n = int(input())
L = list(map(int, input().split()))
a = 1
m = 0
v = L[0]
for i in range(1, n):
    if L[i] >= v:
        a += 1
    else:
        if a > m:
            m = a
        a = 1
    v = L[i]
print(max([a, m]))
