n = int(input())
s = input().rstrip()
i = 0
while i < n:
    if s[i] != 'o':
        print(s[i], end='')
    else:
        j = i + 1
        while j < n - 1 and s[j] == 'g' and (s[j + 1] == 'o'):
            j += 2
        if j != i + 1:
            print('***', end='')
        else:
            print(s[i], end='')
        i = j - 1
    i += 1
