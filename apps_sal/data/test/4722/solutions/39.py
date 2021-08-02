a, b = list(map(int, input().split()))
if a % 3 == 0 or b % 3 == 0:
    print("Possible")
elif a % 3 == 1 and b % 3 == 2:
    print("Possible")
elif a % 3 == 2 and b % 3 == 1:
    print("Possible")
else:
    print("Impossible")
