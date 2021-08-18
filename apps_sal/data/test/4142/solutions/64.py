step = input()


s = list(step)

odd_list = s[0::2]
even_list = s[1::2]

if 'L' in odd_list or 'R' in even_list:
    print('No')
else:
    print('Yes')
