from collections import Counter
(n, d) = map(int, input().split())
x = sorted(map(int, input().split()))
freq = list(Counter(x).items())
freq.sort(key=lambda pair: pair[0])
toleft = 0
mindrop = n
for (i, x) in enumerate(freq):
    toleft += freq[i - 1][1] if i > 0 else 0
    toright = sum([pair[1] for pair in freq[i + 1:] if pair[0] > x[0] + d])
    mindrop = min(toleft + toright, mindrop)
print(mindrop)
