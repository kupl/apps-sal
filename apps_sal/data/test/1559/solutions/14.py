n = int(input())
s = input()
s = str(int(s) + 1)
l = len(s)
if(n == l):
    print(s)
elif(n > l):
    print(str("1" + "0" * (n - 1)))

elif(l % n != 0):
    print(str("1" + "0" * (n - 1)) * (l // n + 1))
else:
    d = s[:n]
    i = n
    flag = 0
    while(i < l):
        z = s[i:i + n]
        if(int(z) > int(d)):
            d = str(int(d) + 1)
            flag = 1
            break
        i = i + n
    print(str(d) * int(l // n))
