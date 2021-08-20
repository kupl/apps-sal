o = input()
t = input()
ans = ''
for i in range(min(len(o), len(t))):
    ans += o[i] + t[i]
if len(o) > len(t):
    ans += o[-1]
elif len(o) < len(t):
    ans += t[-1]
else:
    pass
print(ans)
