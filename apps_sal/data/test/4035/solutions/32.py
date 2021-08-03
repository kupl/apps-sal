A, B = map(int, input().split())
l = []
for i in range(1, 10000):
    a = i * 0.08
    b = i * 0.1
    if a > A + 1 and b > B + 1:
        break
    elif A <= a < A + 1 and B <= b < B + 1:
        l.append(i)

if len(l) == 0:
    print(-1)
else:
    print(min(l))
