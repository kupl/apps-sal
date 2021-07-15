n, pos, l, r = list(map(int, input().split()))

l_close = l == 1
r_close = r == n
ans = 0
if l_close and r_close:
	pass
elif l_close:
	ans += abs(pos - r) + 1
elif r_close:
	ans += abs(pos - l) + 1
else:
	ans += min(abs(pos - r), abs(pos - l)) + 1 + abs(l - r) + 1

print(ans)

