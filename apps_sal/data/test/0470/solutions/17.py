m = list(map(int, input().split()))
m.sort(reverse=True)
count = 1
now = m[0]
sums = [0]
for i in range(1, 5):
    if m[i] == now:
        count += 1
    else:
        if count == 2:
            sums.append(2 * now)
        elif count > 2:
            sums.append(3 * now)
        now = m[i]
        count = 1
if count == 2:
    sums.append(2 * now)
elif count > 2:
    sums.append(3 * now)
ans = sum(m) - max(sums)
print(ans)
