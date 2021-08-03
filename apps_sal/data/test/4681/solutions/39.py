N = int(input())
L = [2, 1]
i = 0
while i < N:
    buff = L[0]
    L[0] = L[1]
    L[1] += buff
    i += 1
print((L[0]))
