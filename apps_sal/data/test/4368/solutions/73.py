N, K = map(int, input().split())

n = 1
while True:
    if K ** (n - 1) <= N < K ** n:
        break
    n += 1

print(n)
return
