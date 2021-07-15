n = int(input())

left = [[] for _ in range(27)]
right = [[] for _ in range(27)]

for i, c in enumerate(input().strip()):
    if c == '?':
        left[26].append(i + 1)
    else:
        left[ord(c) - ord('a')].append(i + 1)
for i, c in enumerate(input().strip()):
    if c == '?':
        right[26].append(i + 1)
    else:
        right[ord(c) - ord('a')].append(i + 1)

result = []
for i in range(26):
    count = min(len(left[i]), len(right[i]))
    for j in range(count):
        result.append((left[i][j], right[i][j]))

i = 0
left_q = 0
while True:
    if left_q == len(left[26]) or i == 26:
        break
    for j in range(len(left[i]), len(right[i])):
        result.append((left[26][left_q], right[i][j]))
        left_q += 1
        if left_q == len(left[26]):
            break
    i += 1

i = 0
right_q = 0
while True:
    if right_q == len(right[26]) or i == 26:
        break
    for j in range(len(right[i]), len(left[i])):
        result.append((left[i][j], right[26][right_q]))
        right_q += 1
        if right_q == len(right[26]):
            break
    i += 1

while left_q < len(left[26]) and right_q < len(right[26]):
    result.append((left[26][left_q], right[26][right_q]))
    left_q += 1
    right_q += 1

print(len(result))
for i, j in result:
    print(i, j)

