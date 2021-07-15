n = int(input())
if n < 5:
	print(n * (n-1) // 2)
	return
val = 5
while n >= val * 10:
	val *= 10
# print(val, nines)
ans = 0
_val = val
while _val <= n:
	ans += min(n - _val+1, _val - 1)
	_val += val
print(ans)
