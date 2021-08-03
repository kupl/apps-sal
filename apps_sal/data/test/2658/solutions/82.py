n, k = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
prev = 0
count = 0
used = {prev: count}
for _ in range(min(k, n)):
    prev = A[prev]
    count += 1
    if prev in used:
        break
    used[prev] = count
if count > used[prev]:
    for _ in range((k - used[prev]) % (count - used[prev])):
        prev = A[prev]
print(prev + 1)
