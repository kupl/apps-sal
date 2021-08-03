n = int(input())
s = input()

diff = 0
min_diff = 0

for i in range(n):
    if s[i] == "(":
        diff += 1
    else:
        diff -= 1
        min_diff = min([min_diff, diff])

if min_diff >= -1 and diff == 0:
    print("Yes")
else:
    print("No")
