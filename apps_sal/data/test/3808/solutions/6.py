import sys

input()
c = input()


if not "(" in c:
    print("No")
    return

last = c.rfind("(")

corr = "(" + c[:last] + c[last + 1 :]

sums = 0
for br in corr:
    if br == "(":
        sums += 1
    else:
        sums -= 1
    if sums < 0:
        print("No")
        return

print("Yes" if sums == 0 else "No")


