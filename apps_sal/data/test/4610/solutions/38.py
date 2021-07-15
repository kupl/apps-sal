from collections import Counter
_, K = map(int, input().split())
A = list(map(int, input().split()))
_, cnt = zip(*Counter(A).most_common()[::-1])
print(sum(cnt[:len(cnt) - K]))
