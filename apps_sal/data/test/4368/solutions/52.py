# abc156b
n, k = map(int, input().split())
for i in range(100):
    if k**i <= n and n <= k**(i + 1) - 1:
        print(i + 1)
        break
