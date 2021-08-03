_ = input()
l = input()
res = 0
for i in range(len(l) - 2):
    if l[i] == l[i + 1] and l[i + 1] == l[i + 2] and l[i] == 'x':
        res += 1
print(res)
