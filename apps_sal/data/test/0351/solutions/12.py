n, k = list(map(int, input().split()))
s = sorted(tuple(map(int, input().split())))
max = k
ans = 0
for a in s:
    if a > max:
        while max < a / 2:
            max = max * 2
            ans = ans + 1
        max = a
print(ans)
