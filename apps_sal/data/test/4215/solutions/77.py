(A, B) = map(int, input().split())
ANS = A - B * 2
if ANS <= 0:
    print(0)
else:
    print(ANS)
