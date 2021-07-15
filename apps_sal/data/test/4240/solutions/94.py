string = input()
rotated_string = input()
for i in range(len(string)):
    string = string[-1] + string[0:-1]
    if string == rotated_string:
        print('Yes')
        return
print('No')

