N, M = map(int, input().split())

t = (N - M) * 100 + M * 1900 
print(t * (2 ** M))
