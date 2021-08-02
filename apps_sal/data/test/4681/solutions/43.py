N = int(input())

L = [2, 1]

if N <= 1:
    print(L[N])
    return
else:
    for i in range(N - 1):
        L.append(L[-1] + L[-2])

print(L[-1])
