n, k = map(int, input().split())
p = list(map(int, input().split()))
mu = [(a + 1) / 2 for a in p]
maxsum = sum(mu[:k])
now = maxsum
left = 0
right = k
while right < n:
    now = now + mu[right] - mu[left]
    if maxsum < now:
        maxsum = now
    left += 1
    right += 1
print(maxsum)
