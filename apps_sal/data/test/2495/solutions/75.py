N = int(input())
a = list(map(int, input().split()))
num = float('inf')
for k in [0, 1]:
    s = 0
    tmp = 0
    for i in range(N):
        s += a[i]
        if i % 2 == k:
            if s <= 0:
                tmp += abs(s) + 1
                s = 1
        else:
            if s >= 0:
                tmp += abs(s) + 1
                s = -1
    num = min(tmp, num)

print(num)
