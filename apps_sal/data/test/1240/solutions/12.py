n = int(input())
left = []
right = []
R = 0
L = 0
for i in range(n):
    a, b = map(int, input().split())
    left.append(a)
    L += a
    R += b
    right.append(b)
base = abs(L - R)
m = base
cur = -1
for i in range(n):
    L1 = L - left[i] + right[i]
    R1 = R - right[i] + left[i]
    curm = abs(L1 - R1)
    if curm > m:
        m = curm
        cur = i
print(cur + 1)
