(A, B) = map(int, input().split())
if A >= 13:
    print(B)
elif 6 <= A <= 12:
    print(int(B / 2))
elif A <= 5:
    print('0')
