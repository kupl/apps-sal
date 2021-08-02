o = input()
e = input()

ans = ''
for i in range(len(e)):
    ans += o[i]
    ans += e[i]
if len(e) < len(o):
    ans += o[-1]
print(ans)
