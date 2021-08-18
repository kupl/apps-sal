n = int(input())
s = input().rstrip()
s += "#"
ans = (n - 1) * n // 2
if "A" not in s or "B" not in s:
    print(ans)
    return

cnt = 0
counts = []
for i, ch in enumerate(s):
    if i == 0:
        prev = ch
        cnt += 1
        continue
    if prev == ch:
        cnt += 1
    else:
        counts.append(cnt)
        cnt = 1
    prev = ch

for c1, c2 in zip(counts, counts[1:]):
    ans -= c1 + c2 - 1
print(ans)
