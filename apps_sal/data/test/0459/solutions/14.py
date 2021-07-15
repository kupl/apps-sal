
def ok(v):
	for i in range(0, 24, 4):
		if len(set(v[i:i+4])) > 1:
			return False
	return True

a = list(map(int, input().split()))

v = a[:]
v[2] = a[15]
v[3] = a[13]
v[16] = a[2]
v[18] = a[3]
v[8] = a[18]
v[9] = a[16]
v[13] = a[8]
v[15] = a[9]
if ok(v):
	print('YES')
	return

v = a[:]
v[2] = a[16]
v[3] = a[18]
v[16] = a[9]
v[18] = a[8]
v[8] = a[13]
v[9] = a[15]
v[13] = a[3]
v[15] = a[2]
if ok(v):
	print('YES')
	return

v = a[:]
v[5] = a[13]
v[4] = a[12]
v[17] = a[5]
v[16] = a[4]
v[21] = a[17]
v[20] = a[16]
v[13] = a[21]
v[12] = a[20]

if ok(v):
	print('YES')
	return

v = a[:]
v[5] = a[17]
v[4] = a[16]
v[17] = a[21]
v[16] = a[20]
v[21] = a[13]
v[20] = a[12]
v[13] = a[5]
v[12] = a[4]

if ok(v):
	print('YES')
	return

v = a[:]
v[0] = a[4]
v[2] = a[6]
v[4] = a[8]
v[6] = a[10]
v[8] = a[23]
v[10] = a[21]
v[23] = a[0]
v[21] = a[2]

if ok(v):
	print('YES')
	return

v = a[:]
v[0] = a[23]
v[2] = a[21]
v[4] = a[0]
v[6] = a[2]
v[8] = a[4]
v[10] = a[6]
v[23] = a[8]
v[21] = a[10]

if ok(v):
	print('YES')
	return

print('NO')
