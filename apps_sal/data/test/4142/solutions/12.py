string = input()
main = []
for index, char in enumerate(string):
    if (index + 1) % 2 == 1:
        if char not in 'RUD':
            main.append('No')
    else:
        if char not in 'LUD':
            main.append('No')
            
main.append('Yes')
print((main[0]))

