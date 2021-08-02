A, B = map(int, input().split())

if A == 1 and 13 >= B >= 2:
    print("Alice")
elif B == 1 and 13 >= A >= 2:
    print("Bob")
elif A > B:
    print("Alice")
elif B > A:
    print("Bob")
elif A == B:
    print("Draw")
