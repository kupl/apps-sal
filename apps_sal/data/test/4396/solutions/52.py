N = int(input())
result = 0
for _ in range(N):
    (x, u) = input().split()
    x = float(x)
    if u == 'JPY':
        result += x
    else:
        result += x * (3.8 * 10 ** 5)
print(result)
