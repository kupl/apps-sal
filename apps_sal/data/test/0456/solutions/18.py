l = int(input())
s = input()
l += 2
s += '  '
ret = ''
i = 0
while i < l - 2:
    if s[i] == 'o' and s[i + 1] == 'g' and s[i + 2] == 'o':
        j = i + 3
        while j < l - 1:
            if s[j] == 'g' and s[j + 1] == 'o':
                j += 2
            else:
                break
        ret += '***'
        i = j
    else:
        ret += s[i]
        i += 1
print(ret)
