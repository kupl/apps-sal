cnt = int(input())
string = input()
x = [0]
i = 0
for _ in string:
    if _ == 'I':
        i += 1
        x.append(i)
    else:
        i -= 1
        x.append(i)
print(max(x))
