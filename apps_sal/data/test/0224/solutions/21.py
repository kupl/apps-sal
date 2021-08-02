import sys

LETTERS = {'A', 'E', 'I', 'O', 'U', 'Y'}


line = sys.stdin.readline().strip()

max_count = 0
current_count = 0


for ch in line:
    if ch in LETTERS:
        max_count = max(max_count, current_count)
        current_count = 0
    else:
        current_count += 1

max_count = max(max_count, current_count)
print(max_count + 1)
