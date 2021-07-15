n = int(input())
seq = input().replace(' ', '')
nGTotal = seq.count('G')
nGCur = 0
right = -1
result = 0
for left in range(n):
    if right < left:
        right = left - 1
        nGCur = 0
    while right + 1 < n and ((seq[right + 1] == 'G' and (right - left + 1 - nGCur == 0 or nGCur + 2 <= nGTotal)) or (seq[right + 1] == 'S' and right + 1 - left + 1 - nGCur <= 1 and nGCur + 1 <= nGTotal)):
        right += 1
        if seq[right] == 'G':
            nGCur += 1
    result = max(right - left + 1, result)
    if seq[left] == 'G':
        assert right >= left
        nGCur -= 1
print(result)

