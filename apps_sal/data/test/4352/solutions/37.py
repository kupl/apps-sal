A, B = map(int, input().split())

if A == B:
    print("Draw")
else:
    if B != 1 and A > B\
            or A == 1:
        print("Alice")
    else:
        print("Bob")
