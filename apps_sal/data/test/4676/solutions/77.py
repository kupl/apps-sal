o = str(input())
e = str(input())
ans = ''
judge = False
if len(o) - len(e) == 1:
    judge = True
for i in range(len(e)):
    ans += o[i]
    ans += e[i]
if judge:
    ans += o[-1]
print(ans)
