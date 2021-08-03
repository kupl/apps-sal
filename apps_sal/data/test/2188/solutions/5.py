n = int(input())

v = []
u = []
for i in range(n):
    x = input().split(' ')
    a = int(x[0])
    b = int(x[1])
    if a > b:
        v.append((a, b, i + 1))
    else:
        u.append((a, b, i + 1))

'''nr = 1
sol = [str(v[0][2])]
act = v[0][1]
i = 1
n = len(v)
while i < n:
	while i < n and v[i][0] < act:
		i += 1
	if i < n:
		nr += 1
		sol.append(str(v[i][2]))
		act = v[i][1]
		i += 1

u = sorted(uv, key = lambda x:x[1])
nr2 = 1
sol2 = [str(u[0][2])]
act = u[0][1]
i = 1
n = len(u)
while i < n:
	while i < n and u[i][0] < act:
		i += 1
	if i < n:
		nr2 += 1
		sol2.append(str(u[i][2]))
		act = u[i][1]
		i += 1'''
if len(u) > len(v):
    u = sorted(u, key=lambda x: x[1], reverse=True)
    print(len(u))
    sol = []
    for i in range(len(u)):
        sol.append(str(u[i][2]))
    print(' '.join(sol))
else:
    v = sorted(v, key=lambda x: x[1], reverse=False)
    print(len(v))
    sol = []
    for i in range(len(v)):
        sol.append(str(v[i][2]))
    print(' '.join(sol))
