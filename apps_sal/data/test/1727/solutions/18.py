n = int(input())
posi = []
high = []
for _ in range(n):
    [a, b] = input().strip().split()
    posi.append(int(a))
    high.append(int(b))

if 2 < n:
    ans = 0
    last = posi[0]
    for i in range(1, n - 1):
        h = high[i]
        if posi[i] - h > last:
            ans += 1
            last = posi[i]
        elif posi[i] + h < posi[i + 1]:
            ans += 1
            last = posi[i] + h
        else:
            last = posi[i]
    ans += 2
else:
    ans = n
print(ans)
