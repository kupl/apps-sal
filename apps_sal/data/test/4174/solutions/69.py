(N, X) = map(int, input().split())
L = [int(i) for i in input().split()]
D = [0]
for i in range(N):
    a = D[i] + L[i]
    if a <= X:
        D.append(a)
    else:
        break
print(len(D))
