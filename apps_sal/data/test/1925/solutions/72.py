
def solve(A, B, N):
    x = min(B - 1, N)
    a = A * x // B - A * (x // B)
    return a


A, B, N = list(map(int, input().split()))
print((solve(A, B, N)))
