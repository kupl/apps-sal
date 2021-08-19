s = input()
res = ''
for i in s:
    if i != 'B':
        res += i
    else:
        res = res[:len(res) - 1]
print(res)
