
N = int(input())
A = list(map(int, input().split()))
total = sum(A)
arai = 0
sunuke = 0
ans = float('inf')

for i in range(N - 1):
    sunuke += A[i]
    arai = total - sunuke
    ans = min(ans, abs(sunuke - arai))

print(ans)
