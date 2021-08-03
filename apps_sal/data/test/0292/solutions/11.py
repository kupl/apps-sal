h, n = map(int, input().split())
t = bin(n - 1)[2:]
t = '0' * (h - len(t)) + t
res = 0
flag = True
for i in range(h):
    if(t[i] == ('1' if flag else '0')):
        res += 2**(h - i)
    else:
        flag = not flag
        res += 1
print(res)
