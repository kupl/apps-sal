(a, b) = list(map(int, input().split()))
k = int((a + b) / 2)
if abs(a - k) == abs(b - k):
    print(k)
else:
    print('IMPOSSIBLE')
