R = lambda type_ = "int": list(map(eval(type_), input().split(' ')))

n = int(input())

s = ['o'] * n

i = 1
j = 1

while j <= n:
    s[j - 1] = 'O'
    i, j = j, i + j

print(''.join(s))


