o = input()
e = input()
res = ""
n = min(len(o), len(e))
for i in range(n):
    res += o[i] + e[i]

if len(e) > len(o):
    res += e[-1]
elif len(e) < len(o):
    res += o[-1]

print(res)
