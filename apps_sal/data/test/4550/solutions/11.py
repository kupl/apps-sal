# 47
data = list(input().split())
if (int(data[0]) > int(data[1]) and int(data[0]) > int(data[2])):
    if int(data[0]) == int(data[1]) + int(data[2]):
        print('Yes')
    else:
        print('No')
elif (int(data[1]) > int(data[0]) and int(data[1]) > int(data[2])):
    if int(data[1]) == int(data[0]) + int(data[2]):
        print('Yes')
    else:
        print('No')
elif (int(data[2]) > int(data[1]) and int(data[2]) > int(data[0])):
    if int(data[2]) == int(data[1]) + int(data[0]):
        print('Yes')
    else:
        print('No')
else:
    print('No')
