(N, K) = map(int, input().split())
n = 1
while N >= K ** n:
    n += 1
print(n)
