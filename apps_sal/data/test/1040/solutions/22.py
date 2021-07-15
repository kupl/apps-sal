input()
a=input()
res = ""
for c in a:
	res += c
	if res.endswith("fox"):
		res = res[:-3]
print(len(res))
