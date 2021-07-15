N, K = map(int, input().split())

def count(x):
    if x <= N + 1:
        return x - 1
    else:
        return (x - 1) - 2 * (x - 1 - N)

ans = 0
for x in range(2, 2 * N + 1):
    y = x - K
    if not 2 <= y <= 2 * N:
        continue
    ans += count(x) * count(y)
    
print(ans)
