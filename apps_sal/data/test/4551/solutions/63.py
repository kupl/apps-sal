A, B, C, D = map(int, input().split())
if A+B < C+D:
    print("Right")
elif A+B > C+D:
    print("Left")
else:
    print("Balanced")
