S = input()
S += '*'
st = 'ACGT'
(i, n) = (0, len(S))
max_len = 0
while i < n:
    j = i
    size = 0
    while S[j] in st:
        size += 1
        j += 1
    i = j + 1
    max_len = max(max_len, size)
print(max_len)
