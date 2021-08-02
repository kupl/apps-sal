s = input()
ans = 0
length = 0

for c in s:
    if c in {'A', 'C', 'G', 'T'}:
        length += 1
    else:
        length = 0

    ans = max(length, ans)

print(ans)
