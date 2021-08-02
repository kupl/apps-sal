from collections import Counter

n, k = map(int, input().split())
a = [int(an) for an in input().split()]
ans = 0
set_a = set(a)
num_of_types = len(set_a)
if num_of_types > k:
    cnt = Counter(a)
    ans = sum(sorted(cnt.values())[: num_of_types - k])

print(ans)
