s = input()
tmp = ""
s = s[::-1]
xx = z = it = 0
while it < len(s):
	if s[it] == '2':
		tmp = tmp + '0'*z + '2'
		z = 0
	if s[it] == '0':
		z+=1
	if s[it] == '1':
		xx+=1
	it = it + 1
tmp = tmp + '1'*xx + '0'*z
print(tmp[::-1])
