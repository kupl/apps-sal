def abc(s):
    a = 0
    for i in range(0, len(s), 2):
        if s[i] == 'L':
            a += 1
    for j in range(1, len(s), 2):
        if s[j] == 'R':
            a += 1
    if a == 0:
        return 'Yes'
    else:
        return 'No'


print(abc(input()))
