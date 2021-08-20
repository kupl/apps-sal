o = input()
e = input()
len_o = len(o)
len_e = len(e)
ans = ''
if len_o == len_e:
    for i in range(len_o):
        ans += o[i]
        ans += e[i]
elif len_o > len_e:
    for i in range(len_e):
        ans += o[i]
        ans += e[i]
    for i in range(len_e, len_o):
        ans += o[i]
else:
    for i in range(len_o):
        ans += o[i]
        ans += e[i]
    for i in range(len_o, len_e):
        ans += e[i]
print(ans)
