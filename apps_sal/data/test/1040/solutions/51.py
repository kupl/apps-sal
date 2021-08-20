n = int(input())
s = input()
tmp = ''
result = 0
for word in s:
    tmp += word
    if tmp[-3:] == 'fox':
        result += 1
        tmp = tmp[:-3]
print(len(tmp))
