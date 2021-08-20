(A, B) = list(map(int, input().split()))
if A >= 13:
    print(B)
elif 6 <= A <= 12:
    print(B // 2)
elif 5 >= A:
    print(0)
