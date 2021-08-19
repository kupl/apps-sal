(A, B) = map(int, input().split())
if A + B >= A - B and A + B >= A * B:
    print(A + B)
elif A - B >= A + B and A - B >= A * B:
    print(A - B)
elif A * B >= A + B and A * B >= A - B:
    print(A * B)
