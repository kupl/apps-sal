o = input()
e = input()

res = ""
for i, j in zip(o, e):
    res += i + j
if(len(o) != len(e)):
    res += o[-1]
print(res)
