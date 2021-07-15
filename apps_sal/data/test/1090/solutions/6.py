n, k = [int(i) for i in input().split()]
s = input()

status = s[0]
cnt = 1
sa = []
for i in range(1, n):
    if s[i] != status:
        sa.append(status * cnt)
        cnt = 0
        status = s[i]
    cnt += 1
sa.append(status * cnt)

for i in range(1, min(k*2, len(sa)), 2):
    sa[i] = ("R" if sa[i][0] == "L" else "L") * len(sa[i])

sa = ''.join(sa)

ans = 0
for i in range(n):
    if sa[i] == "L":
        if i > 0: 
            if sa[i-1] == "L": ans += 1
    else:
        if i < n-1:
            if sa[i+1] == "R": ans += 1

print(ans)
