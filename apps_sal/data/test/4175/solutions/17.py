n = int(input())
l = []
w = [0]*n
for i in range(n):
	w[i] = input()
	if w[i] in l:
		print('No')
		return
	l.append(w[i])
	if (i >= 1 and w[i-1][-1] == w[i][0]) or i == 0:
		continue
	else:
		print('No')
		return
print('Yes')
