n = input()
result = ''
for i in n:
    if i == '1':
        result += '9'
    elif i == '9':
        result += '1'
print(result)
