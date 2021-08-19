data = list(input().split())
if data[2] == 'week':
    if data[0] == '5' or data[0] == '6':
        print(53)
    else:
        print(52)
elif int(data[0]) <= 29:
    print(12)
elif data[0] == '30':
    print(11)
else:
    print(7)
