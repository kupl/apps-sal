S = input()
vowels = 'AEIOUY'
S += 'A'
prev_pos = -1
max_jump = 0
for i, ch in enumerate(S):
    if ch in vowels:
        next_pos = i
        max_jump = max(max_jump, next_pos - prev_pos)
        prev_pos = next_pos
print(max_jump)
