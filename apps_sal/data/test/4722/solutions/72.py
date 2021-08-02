A, B = map(int, input().split())

total = A + B

if total % 3 == 0 or A % 3 == 0 or B % 3 == 0:
    print("Possible")
else:
    print("Impossible")
