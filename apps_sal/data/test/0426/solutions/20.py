(a, b) = list(map(int, input().split()))
array = list(input())
changes = 0
x = 0
while changes < b:
    if x == a:
        break
    if x == 0:
        if array[x] == '1':
            pass
        else:
            array[x] = '1'
            changes += 1
    elif array[x] == '0':
        pass
    else:
        array[x] = '0'
        changes += 1
    x += 1
if a == 1:
    if b > 0:
        print(0)
    else:
        print(array[0])
else:
    answer = ''.join(array)
    print(answer)
