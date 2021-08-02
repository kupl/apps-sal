
s = str(input())

a = 0
b = 0

for i in range(len(s)):
    if i % 2 == 0:
        if "L" in s[i]:
            a += 1

for i in range(len(s)):
    if i % 2 != 0:
        if "R" in s[i]:
            b += 1


if a > 0 or b > 0:
    print("No")
else:
    print("Yes")
