n, k = list(map(int, input().split()))
seq = list(sorted(map(int, input().split())))

i = 0
j = n - 1
result = seq[n - 1] - seq[0]

while result > 0:
    if i == j - 1:
        used = (seq[i + 1] - seq[i]) * (i + 1)
    else:
        used = (seq[i + 1] - seq[i] + seq[j] - seq[j - 1]) * (i + 1)
    if used >= k:
        result -= k // (i + 1)
        break
    k -= used
    if i == j - 1:
        result = 0
        break
    result = seq[j - 1] - seq[i + 1]
    i += 1
    j -= 1

print(result)
