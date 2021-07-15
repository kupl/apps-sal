h, m, s, t1, t2 = map(int, input().split())

splits = [False] * 12

m = m // 5
s = s // 5
splits[h%12] = True
splits[m%12] = True
splits[s%12] = True

start = t1 % 12
end = t2 % 12

if start > end:
	a = splits[start:] + splits[:end]
	b = splits[end:start]
else:
	a = splits[:start] + splits[end:]
	b = splits[start:end]

if True in a and True in b:
	print("NO")
else:
	print("YES")
