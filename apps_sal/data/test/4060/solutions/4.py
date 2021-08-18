size = int(input())
seq = input()
offsets = []
if seq[0] == "(":
    offsets.append(1)
else:
    offsets.append(-1)
for char in seq[1:]:
    if char == "(":
        offsets.append(offsets[-1] + 1)
    else:
        offsets.append(offsets[-1] - 1)
min_offsets = [offsets[-1]] * size
for idx in range(size - 2, -1, -1):
    min_offsets[idx] = min(min_offsets[idx + 1], offsets[idx])
counter = 0
for idx, char in enumerate(seq):
    if idx > 0:
        if offsets[idx - 1] < 0:
            break
    proposed_offset = -2
    if char == ")":
        proposed_offset = 2
    if min_offsets[idx] + proposed_offset >= 0 and offsets[-1] + proposed_offset == 0:
        counter += 1
print(counter)
