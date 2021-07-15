n = int(input())
s = input()
ca = cb = cc = cd =0
for c in s:
	ca += (c == 'A')
	cb += (c == 'C')
	cc += (c == 'G')
	cd += (c == 'T')
m = max(ca, cb, cc, cd)
count = (ca == m) + (cb == m) + (cc == m) + (cd == m)
print((count**n) % int(1e9+7))

