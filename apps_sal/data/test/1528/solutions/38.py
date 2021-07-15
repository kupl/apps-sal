N, X = map(int, input().split())

burger = [1]
patty = [1]
for i in range(N):
    burger.append(burger[i]*2 + 3)
    patty.append(patty[i]*2 + 1)
    
def f(N, X):
    if N == 0:
        if X <= 0:
            return 0
        else:
            return 1
    elif X <= burger[N-1] + 1:
        return f(N-1, X-1)
    else:
        return patty[N-1] + 1 + f(N-1, X-2-burger[N-1])

ans = f(N, X)
print(ans)
