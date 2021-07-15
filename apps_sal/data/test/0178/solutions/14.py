s = int(input())
string = input()
counter = 0
array = []
for i in range(len(string)):
    if string[i] == '8':
        counter += 1
        array.append(i)
if (s - 11) // 2 >= counter:
    print('NO')
elif (s - 11) // 2 < counter:
    if array[0] > (s - 11) // 2:
        print('NO')
    elif array[(s - 11) // 2] - ((s - 11) // 2) <= (s - 11) // 2:
        print('YES')
    elif array[(s - 11) // 2] - ((s - 11) // 2) > (s - 11) // 2:
        print('NO')
else:
    print('YES')
