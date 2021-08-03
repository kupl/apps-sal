a = list(map(int, input().split()))
A = a[0]
B = a[1]
C = a[2]

if C > (A - B):
    print(C - A + B)
else:
    print(0)
