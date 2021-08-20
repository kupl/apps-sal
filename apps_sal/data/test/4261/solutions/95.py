(A, B, C) = map(int, input().split())
buf = C - (A - B)
if buf >= 0:
    print(buf)
else:
    print('0')
