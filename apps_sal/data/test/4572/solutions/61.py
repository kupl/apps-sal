S = [s for s in input()]
li = list(set(S))
li.sort()

ans = 'None'
for c in [chr(c) for c in range(97, 123)]:
    if c not in li:
        ans = c
        break
print(ans)
