N = int(input())
H = list(map(int, input().split()))

sbn = 0
maxim = 0
for i in range(1, N):
    if maxim < H[i - 1]:
        maxim = H[i - 1]
    if H[i - 1] > H[i]:
        sbn = maxim - H[i]
    if abs(sbn) > 1:
        print("No")
        return

print("Yes")
