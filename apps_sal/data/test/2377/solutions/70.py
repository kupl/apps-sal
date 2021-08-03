from bisect import bisect_left

N, H = map(int, input().split())
amax = 0
B = []
for i in range(N):
    a, b = map(int, input().split())
    if a > amax:
        amax = a
    B.append(b)

B = sorted(B)
idx = bisect_left(B, amax)
B = B[idx:][::-1]
cum = [0]
for i in range(len(B)):
    cum += [cum[-1] + B[i]]
    if cum[-1] >= H:
        print(i + 1)
        return
print(len(B) + ((H - cum[-1]) + amax - 1) // amax)
