n = int(input())
an = [int(num) for num in input().split()]

one, two, four = 0, 0, 0
for a in an:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1
    else:
        one += 1

if two == 0 and four >= one - 1:
    print("Yes")
elif four >= one:
    print("Yes")
else:
    print("No")
