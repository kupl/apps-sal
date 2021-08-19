(n, k) = map(int, input().split())
stages = sorted(input().strip())
i = 0
total = 0
last = -1
while k > 0 and i < n:
    wi = ord(stages[i]) - ord('a') + 1
    if wi > last + 1:
        total += wi
        k -= 1
        last = wi
    i += 1
if k > 0:
    print(-1)
else:
    print(total)
