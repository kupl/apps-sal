N = int(input())
A = [int(a) for a in input().split()]

def calc(X):
    if X == sorted(X):
        return len(X)
    A = X[:len(X)//2]
    B = X[len(X)//2:]
    return max(calc(A), calc(B))

print(calc(A))

