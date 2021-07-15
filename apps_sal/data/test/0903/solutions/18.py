import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l = sorted(l)
p = n // 2
ans = l[p]
tgt = 1
while (p < n - 1):
	diff = l[p + 1] - l[p]
	if k >= diff * tgt:
		k -= diff * tgt
		p += 1
		ans = l[p]
		tgt += 1
	else:
		print(ans + k // tgt)
		return
print(ans + k // tgt)

