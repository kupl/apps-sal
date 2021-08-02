import sys

n = int(input())
a = [int(x) for x in input().rstrip().split()]

even = 0
odd = 0
num4 = 0
for i in a:
    if i % 4 == 0:
        num4 += 1
        continue

    elif i % 2 == 0:
        even += 1
    else:
        odd += 1


if odd <= num4:
    print("Yes")
elif odd - 1 == num4 and even == 0:
    print("Yes")
elif odd == 0 and 2 <= even:
    print("Yes")
else:
    print("No")
