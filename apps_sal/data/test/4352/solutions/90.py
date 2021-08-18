
alice, bob = list(map(int, input().split()))

if alice == bob:
    print("Draw")
elif (alice == 1) or ((bob != 1) and (alice > bob)):
    print("Alice")
else:
    print("Bob")
