s = input()
t = input()

position_left = 0
seen_left = 0

while seen_left < len(s) and position_left < len(t):
    if t[position_left] == s[seen_left]:
        seen_left += 1
    position_left += 1

if seen_left < len(s):
    print(0)
    return

position_right = len(t) - 1
seen_right = 0

while seen_right < len(s) and position_right >= 0:
    if t[position_right] == s[len(s) - seen_right - 1]:
        seen_right += 1
    position_right -= 1

if position_left <= position_right:
    print(position_right - position_left + 2)
else:
    print(0)
