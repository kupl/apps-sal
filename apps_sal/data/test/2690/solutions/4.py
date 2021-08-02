s = str(input().strip())
d = {}
d['a'] = []
d['b'] = []
d['c'] = []

for i in range(len(s)):
    d[s[i]].append(i)
ans = [0]
try:
    ans.append(abs(d["a"][0] - d["b"][-1]))
    ans.append(abs(d["b"][0] - d["a"][-1]))
except:
    pass
# if(len(d['a'])>0 and len(d['c'])>0):
try:
    ans.append(abs(d["a"][0] - d["c"][-1]))
    ans.append(abs(d["c"][0] - d["a"][-1]))
except:
    pass
# if(len(d['c'])>0 and len(d['b'])>0):
try:
    ans.append(abs(d["c"][0] - d["b"][-1]))
    ans.append(abs(d["b"][0] - d["c"][-1]))
except:
    pass
print(max(ans))
