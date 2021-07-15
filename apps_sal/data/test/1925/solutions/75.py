A, B, N = map(int, input().split())

x = min(B-1, N)
val = A*x//B - A*(x//B)
print(val)
