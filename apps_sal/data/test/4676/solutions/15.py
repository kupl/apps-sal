o = input()
e = input()
ans = []
for i in range(len(e)):
    ans.append(o[i])
    ans.append(e[i])
if len(o) != len(e):
    ans.append(o[-1])
print(''.join(ans))
