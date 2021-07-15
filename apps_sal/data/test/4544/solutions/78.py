from collections import defaultdict

N = int(input())
a = tuple(map(int, input().split()))
cnt = defaultdict(int)

for i in range(N):
	cnt[a[i]-1] += 1
	cnt[a[i]] += 1
	cnt[a[i]+1] += 1
print(max(cnt.values()))
