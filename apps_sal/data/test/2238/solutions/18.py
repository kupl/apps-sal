n = int(input())
string = ''
x = (n - 1) / 2
x = int(x)
diamond = ''
count = 0
count2 = 0
row = 0
string2 = ''
array = []
while row <= x:
    while count < x:
        string += '*'
        count += 1
    while count2 < 2 * row + 1:
        string2 += 'D'
        count2 += 1
    string = string + string2 + string
    row += 1
    count = row
    count2 = 0
    array.append(string)
    string = ''
    string2 = ''
for i in range(1, x + 1):
    array.append(array[x - i])
for i in range(0, n - 1):
    array[i] = array[i] + '\n'
for item in array:
    diamond += item
print(diamond)
