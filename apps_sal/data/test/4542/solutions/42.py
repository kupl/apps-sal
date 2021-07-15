prev = '0'
ans = -1
for c in input():
    if c != prev:
        ans += 1
    prev = c
print(ans)
