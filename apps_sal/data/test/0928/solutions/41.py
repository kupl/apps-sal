n, k = map(int, input().split())
ai = list(map(int, input().split()))
count = 0

r = 0
l = 0
acc = 0

while r < n:
    while r < n:
        acc += ai[r]
        r += 1
        if acc >= k:
            break

    while l < r:
        if acc >= k:
            count += n - r + 1
            acc -= ai[l]
            l += 1
        else:
            break


print(count)
