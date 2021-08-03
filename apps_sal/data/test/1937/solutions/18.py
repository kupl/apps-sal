n = int(input())
b = list(map(int, input().split()))
a1 = []
a2 = []
cur = 0
last = 10**100
for i in range(len(b)):
    if b[i] - cur > last:
        cur = b[i] - last
    a1 += [cur]
    a2 += [b[i] - cur]
    last = b[i] - cur
print(*(a1 + a2[::-1]))
