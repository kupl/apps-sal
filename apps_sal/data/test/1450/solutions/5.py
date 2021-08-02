s = input()
answer = ''
p = 0
o = 1
for i in s:
    if i == '1':
        p = p + 1
for i in s:
    if i == '0':
        answer = answer + '0'
    elif i == '2':
        answer = answer + '1' * (o * p)
        o = 0
        answer = answer + '2'
answer = answer + '1' * (o * p)
print(answer)
