word = input()
odd_v = ['R', 'U', 'D']
odd_list = []
even_v = ['L', 'U', 'D']
even_list = []

for index, i in enumerate(word, 1):
    if index % 2 == 1:
        odd_list.append(i)
    else:
        even_list.append(i)

if set(odd_list).issubset(odd_v) and set(even_list).issubset(even_v):
    print('Yes')
else:
    print('No')
