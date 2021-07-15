N, X = list(map(int, input().split()))

size = [1]
patty = [1]
for i in range(N):
    size.append(size[i]*2 + 3)
    patty.append(patty[i]*2 + 1)

def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= size[N-1] + 1:
        return f(N-1, X-1)
    elif X == size[N-1] + 2:
        return patty[N-1] + 1
    elif X >= size[N-1] + 3:
        return patty[N-1] + 1 + f(N-1, X-size[N-1]-2)
print((f(N,X)))

