K, X = map(int, input().split())

if X - K + 1 >= -1000000:
    min = X - K + 1
else:
    min = -1000000

if X + K - 1 <= 1000000:
    max = X + K - 1
else:
    max = 1000000

ans = []
for i in range(min, max + 1):
    ans.append(str(i))

print(" ".join(ans))
