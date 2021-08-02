a, b = [int(x) for x in input().split()]
if a == 1:
    a = 14
if b == 1:
    b = 14
if a < b:
    print("Bob")
elif a > b:
    print("Alice")
else:
    print("Draw")
