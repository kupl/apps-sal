o = input()
e = input()
ans = []
for i in range(len(o) + len(e)):
    if i % 2 == 0:
        ans.append(o[i // 2])
    else:
        ans.append(e[i // 2])
print(''.join(ans))
