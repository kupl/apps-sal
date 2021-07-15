n,k = map(int,input().split(" "))
s = list(input())
s1 = s[:]
s2 = sorted(list(set(s)))

if k == 1:
	for ch in s2:
		if s1[0] < ch:
			print(ch)
			return

if n < k:
	s1.extend([s2[0]]*(k-n))
	t = "".join(s1)
	print(t)

else:
	for i in range(k-1,-1,-1):
		if s1[i] != s2[-1]:
			ans = s1[:i]
			ans.append(s2[s2.index(s1[i])+1])
			ans.extend([s2[0]]*(k-i-1))
			print("".join(ans))
			return
