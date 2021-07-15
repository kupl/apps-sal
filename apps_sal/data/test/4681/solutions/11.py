N = int(input())

L = [2, 1]

for i in range(N-1):
    if i == 0:
        L.append(L[0] + L[1])
    else:
        L.append(L[i] + L[i+1])

print((L[-1]))

