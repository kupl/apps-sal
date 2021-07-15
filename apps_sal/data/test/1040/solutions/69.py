N = int(input())
s = input()
tmp = ''
for i in s:
    tmp += i
    if len(tmp) >= 3 and tmp[-3] + tmp[-2] + tmp[-1] == 'fox':
        tmp = tmp[:-3]
print(len(tmp))
