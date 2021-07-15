fact = [1.0, 1.0,2.0,6.0, 24.0, 120.0, 720.0, 5040.0, 40320.0, 362880.0, 3628800.0]
s = input()
s1 = input()
k, k1, kv = 0, 0, 0
for c in s:
	if c == '+':
		k += 1
	else:
		k -= 1
for c in s1:
	if c == '+':
		k1 += 1
	if c == '-':
		k1 -= 1
	if c == '?':
		kv += 1

d = k - k1
if d < 0:
	d = -d
if (d > kv) or ((d % 2) and not(kv % 2)):
	print(0.0)
else:
	if (d == 0) and (kv == 0):
		print(1.0)
	else:
		print(fact[kv] / fact[int((kv - d) / 2)] / fact[kv - int((kv - d) / 2)] / (2.0**kv))
