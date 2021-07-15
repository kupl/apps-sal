a, b = map(int, input().split())

if int(a) == 1 and int(b) != 1:
    print("Alice")
elif int(a) != 1 and int(b) == 1:
    print("Bob")
elif int(a) > int(b):
    print("Alice")
elif int(a) < int(b):
    print("Bob")
elif int(a) == int(b):
    print("Draw")
