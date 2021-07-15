o = input()
e = input()
ans = ''
if len(o) == len(e):
    time = len(o) * 2
else:
    time = len(o) * 2 - 1
for i in range(time):
    if i % 2 == 0:
        ans += o[i // 2]
    else:
        ans += e[i // 2]
print(ans)
