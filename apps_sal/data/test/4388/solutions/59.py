n = int(input())
lst_n = list(str(n))
for i in range(len(lst_n)):
    if lst_n[i] == '1':
        lst_n[i] = '9'
    elif lst_n[i] == '9':
        lst_n[i] = '1'
print(''.join(lst_n))
