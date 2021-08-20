n = int(input())
chairs = input()
if n > 2:
    if chairs.startswith('00') or chairs.endswith('00'):
        print('No')
    elif '000' in chairs or '11' in chairs:
        print('No')
    else:
        print('Yes')
elif chairs == '00' or chairs == '11' or chairs == '0':
    print('No')
else:
    print('Yes')
