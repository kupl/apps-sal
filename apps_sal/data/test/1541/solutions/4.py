s = input()

pivot_pos = 0
left_count = 0
right_count = 0

''''def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
		return False'''

# Find the pivot
for i in range(len(s)):
    if s[i] == '^':
        pivot_pos = i

# Solve left side
for i in range(pivot_pos):
    if s[i].isdigit() == True:
        left_count = left_count + (int(s[i]) * (pivot_pos - i))

# Solve left side
for i in range(pivot_pos, len(s)):
    if s[i].isdigit() == True:
        right_count = right_count + (int(s[i]) * (i - pivot_pos))

if left_count == right_count:
    print("balance")
elif left_count > right_count:
    print("left")
else:
    print("right")
