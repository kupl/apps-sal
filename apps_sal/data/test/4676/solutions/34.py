o = input()
e = input()
ans = ''
for (i, j) in zip(o, e):
    ans += i + j
if len(o) != len(e):
    ans += o[-1]
print(ans)
