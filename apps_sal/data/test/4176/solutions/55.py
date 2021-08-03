A, B = map(int, input().split())
if A > B:
    a = A
    b = B
else:
    a = B
    b = A
r = 1
while r > 0:
    r = a % b
    a = b
    b = r
print(A * B // a)
