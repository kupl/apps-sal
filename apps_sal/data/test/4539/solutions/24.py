N = input()
def f(X): return sum(int(x) for x in X)


print(('Yes' if int(N) % f(N) == 0 else 'No'))
