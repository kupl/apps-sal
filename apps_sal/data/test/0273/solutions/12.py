name, fam = input().split()
ans = name[0]
for ch in name[1:]:
    if ch < fam[0]:
        ans += ch
    else:
        break
ans += fam[0]
print(ans)

