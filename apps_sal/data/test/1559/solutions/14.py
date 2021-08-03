# from time import time
# start = time()
n = int(input())
s = input()
s = str(int(s) + 1)
# print(s)
l = len(s)
# print(l)
if(n == l):
    print(s)
elif(n > l):
    print(str("1" + "0" * (n - 1)))

elif(l % n != 0):
    print(str("1" + "0" * (n - 1)) * (l // n + 1))
else:
    d = s[:n]
    # print(d)
    i = n
    flag = 0
    while(i < l):
        z = s[i:i + n]
        # print(i,d,z)
        if(int(z) > int(d)):
            d = str(int(d) + 1)
            flag = 1
            break
        i = i + n
    # print(l//n)
    print(str(d) * int(l // n))
# end = time()
# print("%0.2f" %(end-start),"seconds")
