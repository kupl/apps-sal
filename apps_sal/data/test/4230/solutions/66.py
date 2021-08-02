X, N = map(int, input().split())
*P, = map(int, input().split())
print(min([i for i in range(102)if(i in P) ^ 1], key=lambda i: abs(i - X)))
