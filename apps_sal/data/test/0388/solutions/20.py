names = list("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Ab Bb Cb Db Eb Fb Gb Hb Ib Jb Kb Lb Mb Nb Ob Pb Qb Rb Sb Tb Ub Vb Wb Xb Gh Rg Df".split())

n, k = map(int, input().split())
A = list(input().split())
find = False
ans = [0] * n
for i in range(n - k + 1):
	s = A[i]
	if find:
		if s == "YES":
			c = 0
			while (names[c] in ans[i:]):
				c += 1
			ans[i + k - 1] = names[c]
		else:
			ans[i + k - 1] = ans[i]
	else:
		if s == "NO":
			ans[i] = names[0]
		else:
			now = i
			for j in range(k):
				ans[now] = names[j]
				now += 1
			find = True
if not find:
	for i in range(n - k + 1, n):
		ans[i] = names[0]
print(" ".join(ans))
