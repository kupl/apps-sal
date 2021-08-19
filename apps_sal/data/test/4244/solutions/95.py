a = 0
b = 0
N = int(input())
X = list(map(int, input().split()))
avg = sum(X) // N
for tai in X:
    a += (tai - avg) ** 2
for tai in X:
    b += (tai - (avg + 1)) ** 2
if a > b:
    print(b)
else:
    print(a)
