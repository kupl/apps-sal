(A, B) = list(map(int, input().split()))
if A >= 13:
    print(B)
elif 6 <= A <= 12:
    print(int(B / 2))
else:
    print(0)
