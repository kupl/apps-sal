A, B = map(int, input().split())
if A + B >= 24:
    print(A + B - 24)
elif A + B < 24:
    print(A + B)
