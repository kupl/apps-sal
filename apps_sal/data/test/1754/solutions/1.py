n, m, k = list(map(int, input().split()))
p = list(map(int, input().split()))
s = list(map(int, input().split()))
good = list(map(int, input().split()))
is_good = [0] * n
for el in good:
	is_good[el - 1] = 1
sch = [[] for i in range(m + 1)]
for i in range(n):
	sch[s[i]].append((p[i], i))
cnt = 0
for el in sch:
	el.sort(reverse=True)
	for i in el[1:]:
		cnt += is_good[i[1]]
print(cnt)



# sorted(i * i for i in range(n))

