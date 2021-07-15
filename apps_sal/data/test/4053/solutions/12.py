def mi():
	return list(map(int, input().split()))
'''

'''
n = int(input())
a = [[] for i in range(n-1)]
aa = [0]*(2*n-2)
ba = [0]*(2*n-2)
for i in range(2*n-2):
	s = input()
	a[len(s)-1].append(s)
	aa[i] = s
	ba[2*n-3-i] = s
s1 = ['0']*n
s2 = ['0']*n
s1[0] = a[0][0]
s1[-1] = a[0][1]
s2[0] = a[0][1]
s2[-1] = a[0][0]
noans1 = False
noans2 = False
t1a = [0]*(2*n-2)
t2a = [0]*(2*n-2)
t1a[aa.index(a[0][0])] = 'P'
t1a[2*n-3-ba.index(a[0][1])] = 'S'
t2a[aa.index(a[0][0])] = 'S'
t2a[2*n-3-ba.index(a[0][1])] = 'P'
# print (aa, ba)
# print (a[1])
for i in range(1,n-1):
	ent1 = False
	# print (t1a)
	t1 = ''.join(s1)
	t2 = ''.join(s2)
	# print (t1, a[i][0][:-1], a[i][1][1:], a[i][0], a[i][1])
	if t1.startswith(a[i][0][:-1]) and t1.endswith(a[i][1][1:]):
		ent1 = True
		s1[i] = a[i][0][-1]
		s1[n-1-i] = a[i][1][0]
		# print (aa.index(a[i][0]), a[i][0])
		# print (2*n-3-ba.index(a[i][1]), a[i][1])
		t1a[aa.index(a[i][0])] = 'P'
		t1a[2*n-3-ba.index(a[i][1])] = 'S'
		# print (2*n-3-ba.index(a[i][1]))
	elif t1.startswith(a[i][1][:-1]) and t1.endswith(a[i][0][1:]):
		ent1 = True
		s1[i] = a[i][1][-1]
		s1[n-1-i] = a[i][0][0]
		t1a[aa.index(a[i][0])] = 'S'
		# print (aa.index(a[i][1]), a[i][1])
		t1a[2*n-3-ba.index(a[i][1])] = 'P'
		# print (2*n-3-ba.index(a[i][0]), a[i][0])
	if ent1==False:
		noans1 = True
	ent2 = False
	if t2.startswith(a[i][0][:-1]) and t2.endswith(a[i][1][1:]):
		ent2 = True
		s2[i] = a[i][0][-1]
		s2[n-1-i] = a[i][1][0]
		# print (aa.index(a[i][0]), a[i][0])
		# print (n-1-ba.index(a[i][1]), a[i][1])
		t2a[aa.index(a[i][0])] = 'P'
		t2a[2*n-3-ba.index(a[i][1])] = 'S'
	elif t2.startswith(a[i][1][:-1]) and t2.endswith(a[i][0][1:]):
		ent2 = True
		s2[i] = a[i][1][-1]
		s2[n-1-i] = a[i][0][0]
		# print (aa.index(a[i][1]), a[i][1])
		# print (n-1-ba.index(a[i][0]), a[i][0])
		t2a[aa.index(a[i][0])] = 'S'
		t2a[2*n-3-ba.index(a[i][1])] = 'P'
	if ent2==False:
		noans2 = True
# print (s1, noans1, s2, noans2)
# print (t1a, t2a)
if noans1:
	print(''.join(t2a))
else:
	print(''.join(t1a))

