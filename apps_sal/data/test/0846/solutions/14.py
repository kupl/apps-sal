n, m = list(map(int, input().split()))
out = [-1] * n
bulbs = list(map(int, input().split()))
for i in bulbs:
    j = i - 1
    while j < n and out[j] == -1:
        out[j] = str(i)
        j += 1
print(' '.join(out))
