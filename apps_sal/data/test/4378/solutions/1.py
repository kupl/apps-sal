input()
garor = list(input())
gar = garor.copy()
for i in range(1, len(gar)):
    if gar[i] == gar[i - 1]:
        options = ['R', 'G', 'B']
        options.remove(gar[i - 1])
        if i < len(gar) - 1 and gar[i + 1] in options:
            options.remove(gar[i + 1])
        gar[i] = options[0]
count = 0
for i in range(0, len(gar)):
    if gar[i] != garor[i]:
        count = count + 1
print(count)
str1 = ''.join(gar)
print(str1)
