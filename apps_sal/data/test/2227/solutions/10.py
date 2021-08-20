input_str = input()
if input_str.find('heavy') == -1:
    print(0)
else:
    a = input_str.index('heavy') + 5
    b = 1
    result = 0
    while a < len(input_str):
        if input_str[a:a + 5] == 'heavy':
            b += 1
            a += 4
        elif input_str[a:a + 5] == 'metal':
            result += b
            a += 4
        else:
            a += 1
    print(result)
