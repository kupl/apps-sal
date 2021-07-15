s = input()

count = 0
ans = 0

for i in s:
    if i in {'A', 'T', 'C', 'G'}:
        count += 1
    else:
        count = 0
    ans = max(ans, count)

print(ans)
