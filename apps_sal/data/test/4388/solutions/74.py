n = input()
n_list = list(n)
for i in range(3):
    if n_list[i] == '1':
        n_list[i] = '9'
    elif n_list[i] == '9':
        n_list[i] = '1'
n_c = ''.join(n_list)
print(n_c)
