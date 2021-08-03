n = int(input())
dict1 = {}
s = str(input())
flag = 0
if(n == 1):
    print("Yes")
else:
    for i in range(n):
        try:
            dict1[s[i]] += 1
            flag = 1
        except:
            KeyError
            dict1[s[i]] = 1
    if(flag == 0):
        print("No")
    else:
        print("Yes")
