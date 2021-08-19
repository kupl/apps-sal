(a, b) = map(float, input().strip().split())
if a % 5 == 0 and b >= a + 0.5:
    print('{:.2f}'.format(b - a - 0.5))
else:
    print('{:.2f}'.format(b))
