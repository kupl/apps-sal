x, y = list(map(str, input().split()))

dict_num = {'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15}

if dict_num[x] == dict_num[y]:
    print('=')
elif dict_num[x] > dict_num[y]:
    print('>')
else:
    print('<')

