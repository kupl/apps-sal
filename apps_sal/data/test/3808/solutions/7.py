n = int(input())
present = input().rstrip()
level = 0
min_level = 0
for ch in present:
    if ch == '(':
        level += 1
    else:
        level -= 1
        min_level = min(min_level, level)
if min_level >= -1 and level == 0:
    print('Yes')
else:
    print('No')
