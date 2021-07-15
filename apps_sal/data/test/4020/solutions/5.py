s = input().split(':')
s1 = input().split(':')
ch1 = int(s[0])
m1 = int(s[1])
ch2 = int(s1[0])
m2 = int(s1[1])
vr1 = ch1 * 60 + m1
vr2 = ch2 * 60 + m2
rz = vr2 - vr1
rz //= 2
ch1 = ch1 * 60 + m1 + rz
chas = ch1 // 60
mn = ch1 - chas * 60
if chas < 10:
	s = '0'
	s += str(chas)
	chas = s
if mn < 10:
	s = '0'
	s += str(mn)
	mn = s
print(chas, mn, sep = ":")

