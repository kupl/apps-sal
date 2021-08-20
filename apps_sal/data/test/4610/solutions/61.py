(N, K) = map(int, input().split())
A = list(map(int, input().split()))
count = {}
for val in A:
    if val in count:
        count[val] += 1
    else:
        count[val] = 1
ans = 0
diff = len(set(A)) - K
if diff > 0:
    count_sorted = sorted(count.items(), key=lambda x: x[1])
    for (k, v) in count_sorted:
        ans += v
        diff -= 1
        if diff == 0:
            break
print(ans)
