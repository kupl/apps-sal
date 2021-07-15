def grundy(a, k):
    while a >= k and a % k:
        b = a % k
        c = a//k + 1
        a += c * (-b // c)
    if a % k == 0:
        return a // k
    return 0
    
N = int(input())
s = 0
for _ in range(N):
    a, k = map(int, input().split())
    s ^= grundy(a, k)

print("Takahashi" if s else "Aoki")
