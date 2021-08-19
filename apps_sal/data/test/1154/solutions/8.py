(n, h, k) = list(map(int, input().split()))
a = [int(x) for x in input().split()]
moulin = 0
ans = 0
for x in a:
    if moulin + x <= h:
        moulin += x
    else:
        ready = (x - h + moulin + k - 1) // k
        passed = min(ready, (moulin + k - 1) // k)
        ans += passed
        moulin = max(0, moulin - k * passed)
        moulin += x
ans += (moulin + k - 1) // k
print(ans)
