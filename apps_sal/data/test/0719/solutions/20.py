k = int(input())
def s(x):
	r = 0
	while x:
		r += x % 10
		x //= 10
	return r
res = 19
if k >= 8000:
	res = 9010000
	k -= 7999
if k > 7500:
	res = 4302001
	k -= 7500

if k > 5000:
	res = 2000017
	k -= 5000


while k > 1:
	res += 9
	if s(res) == 10:
		k -= 1
print(res)

