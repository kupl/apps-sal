n = int(input())
seq = [int(x) for x in input().split()]

# print(seq)

def inseri(s, n):
	if n in s:
		s.remove(n)
		inseri(s, n+1)
	else:
		s.add(n)


s = set()
for i in seq:
	inseri(s, i)

m = max(s)
print(m-len(s)+1)
# print(s)

