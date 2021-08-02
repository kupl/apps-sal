n = int(input())
s = input()

max_subs = 0
num0 = 0
num1 = 0
diffs = {0: 0}
for i, x in enumerate(s):
    if x == '0':
        num0 += 1
    else:
        num1 += 1
    diff = num0 - num1

    if diff in diffs:
        subs = i - diffs[diff] + 1
        if subs > max_subs:
            max_subs = subs
    else:
        diffs[diff] = i + 1

print(max_subs)
