n = int(input())
mas = list(map(str, input().split()))
zero = ''
nepr = '1'
for i in range(n):
    if mas[i] == '0':
        print(0)
        return
    elif mas[i].count('0') == len(mas[i]) - 1 and mas[i][0] == '1':
        zero += '0' * mas[i].count('0')
    else:
        nepr = mas[i]

print(nepr + zero)
