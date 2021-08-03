n = list(map(int, list(input())))
ln = len(n)
ans = 0
for i in range(-1, -ln, -1):
    if n[i] == 10:
        n[i - 1] += 1
        continue
    elif n[i] < 5:
        ans += n[i]
    elif n[i] > 5:
        ans += 10 - n[i]
        n[i - 1] += 1
    else:
        if n[i - 1] < 5:
            ans += 5
        else:
            ans += 5
            n[i - 1] += 1
if n[0] == 10:
    ans += 1
elif n[0] <= 5:
    ans += n[0]
else:
    ans += 11 - n[0]

print(ans)
