s = input()
back = 0
now = 0
after_ab = 0
for i in s:
    if i == 'a':
        back += 1
        after_ab = max(after_ab, now) + 1
    else:
        now = max(back, now) + 1
print(max(back, max(now, after_ab)))
