n = int(input())
dict1 = {}
flag = 0
dict1[n] = 1
while flag == 0:
    n += 1
    while n % 10 == 0:
        n = n // 10
    try:
        dict1[n] += 1
        flag = 1
    except:
        KeyError
        dict1[n] = 1
print(len(dict1))
