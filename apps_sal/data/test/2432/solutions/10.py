n = int(input())
c = bin(n)[2:]
while(len(c)) < 6:
    c = '0' + c
d = ""
d = d + c[0]
d = d + c[5]
d = d + c[3]
d = d + c[2]
d = d + c[4]
d = d + c[1]
print(int(d, 2))
