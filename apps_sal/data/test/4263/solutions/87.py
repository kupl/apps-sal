s = input()

mx = 0
cnt = 0

for (i, char) in enumerate(s):
    if char in "ACGT":
        cnt += 1
    else:
        mx = max(mx, cnt)
        cnt = 0

mx = max(cnt, mx)

print(mx)
