s = input()
pivot_pos = 0
left_count = 0
right_count = 0
"'def is_number(s):\n    try:\n        float(s)\n        return True\n    except ValueError:\n        return False\n    try:\n        import unicodedata\n        unicodedata.numeric(s)\n        return True\n    except (TypeError, ValueError):\n\t\treturn False"
for i in range(len(s)):
    if s[i] == '^':
        pivot_pos = i
for i in range(pivot_pos):
    if s[i].isdigit() == True:
        left_count = left_count + int(s[i]) * (pivot_pos - i)
for i in range(pivot_pos, len(s)):
    if s[i].isdigit() == True:
        right_count = right_count + int(s[i]) * (i - pivot_pos)
if left_count == right_count:
    print('balance')
elif left_count > right_count:
    print('left')
else:
    print('right')
