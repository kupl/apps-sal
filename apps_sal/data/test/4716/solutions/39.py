(N, K) = map(int, input().split())
l = sorted(map(int, input().split()))[::-1]
sum = 0
count = 0
for L in l:
    count += 1
    sum += L
    if count == K:
        break
print(sum)
