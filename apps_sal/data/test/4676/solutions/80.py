o = input()
e = input()
ans = "".join([o[i] + e[i] for i in range(min(len(o), len(e)))])
if len(o) != len(e):
    if len(o) > len(e): ans += o[-1]
    else: ans += e[-1]
print(ans)
