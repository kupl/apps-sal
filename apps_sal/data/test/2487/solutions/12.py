N = int(input())
ANS = 0
for i in range(1, N + 1):
    ANS += i * (i + 1) // 2
for i in range(N - 1):
    (x, y) = sorted(map(int, input().split()))
    ANS -= x * (N - y + 1)
print(ANS)
