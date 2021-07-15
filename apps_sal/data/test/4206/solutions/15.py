s = input().strip()

have_one = 0
have_two = 0
res = 0

for c in s:
    x = int(c)
    if x % 3 == 1:
        have_one += 1
    elif x % 3 == 2:
        have_two += 1
    else:
        res += 1
        have_one = 0
        have_two = 0

    if have_one == 3 or have_two == 3 or (have_one > 0 and have_two > 0):
        res += 1
        have_one = 0
        have_two = 0

print(res)

