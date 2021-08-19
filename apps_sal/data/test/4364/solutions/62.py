s = input()
mae = int(s[:2])
ushiro = int(s[2:])
if 1 <= mae <= 12:
    if 1 <= ushiro <= 12:
        ans = 'AMBIGUOUS'
    else:
        ans = 'MMYY'
elif 1 <= ushiro <= 12:
    ans = 'YYMM'
else:
    ans = 'NA'
print(ans)
