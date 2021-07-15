s = input()

l = len(s)
center = s[l // 2]
cnt = l % 2
for e1, e2 in zip(s[:l//2][::-1], s[l//2+l%2:]):
    if center == e1 == e2:
        cnt += 2
    else:
        break

ans = (l + cnt) // 2
print(ans)

