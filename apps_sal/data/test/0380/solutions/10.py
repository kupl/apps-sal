a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

if (a[0] == b[0] and b[0] == c[0]) or (a[1] == b[1] and b[1] == c[1]):
    print(1)
    return

if (a[0] == b[0] and ((c[1] >= a[1] and c[1] >= b[1]) or (c[1] <= a[1] and c[1] <= b[1]))) or \
   (a[0] == c[0] and ((b[1] >= a[1] and b[1] >= c[1]) or (b[1] <= a[1] and b[1] <= c[1]))) or \
   (c[0] == b[0] and ((a[1] >= c[1] and a[1] >= b[1]) or (a[1] <= b[1] and a[1] <= c[1]))) or \
   (a[1] == b[1] and ((c[0] >= a[0] and c[0] >= b[0]) or (c[0] <= a[0] and c[0] <= b[0]))) or \
   (a[1] == c[1] and ((b[0] >= a[0] and b[0] >= c[0]) or (b[0] <= a[0] and b[0] <= c[0]))) or \
   (b[1] == c[1] and ((a[0] >= c[0] and a[0] >= b[0]) or (a[0] <= b[0] and a[0] <= c[0]))):
    print(2)
    return

print(3)
