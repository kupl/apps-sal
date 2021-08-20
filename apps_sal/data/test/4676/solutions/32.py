o = input()
e = input()
ans = ''
for i in range(len(e)):
    ans += o[i]
    ans += e[i]
if len(o) == len(e):
    print(ans)
else:
    print(ans + o[-1])
