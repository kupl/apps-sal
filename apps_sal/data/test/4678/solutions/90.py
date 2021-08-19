N = int(input())
As = list(map(int, input().split()))
(tlest, total) = (As[0], 0)
for i in range(1, N):
    tlest = max(tlest, As[i])
    if tlest - As[i]:
        total += tlest - As[i]
print(total)
