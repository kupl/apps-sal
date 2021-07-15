n, m = (int(x) for x in input().split())
st = set()
for i in range(n):
	s = input()
	g = s.index('G')
	s = s.index('S')
	if g > s:
		print(-1)
		return
	st.add(s - g)
print(len(st))

