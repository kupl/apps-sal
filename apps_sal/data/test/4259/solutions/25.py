K = int(input())
A, B = map(int, input().split())

TOP = B // K
BOTTOM = (A - 1) // K
d = TOP - BOTTOM
if d > 0:
    print("OK")
else:
    print("NG")
