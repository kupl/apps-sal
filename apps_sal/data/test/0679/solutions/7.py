def go():
    s = input()
    x = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
    for i in x:
        if i in s:
            return 'Yes'
    return 'No'


print(go())
