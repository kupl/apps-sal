a, b = map(int, input().split())
if a == b:
    print("Draw")
elif b != 1 and a != b:
    if a > b or a == 1:
        print("Alice")
    else:
        print("Bob")
else:
    print("Bob")
