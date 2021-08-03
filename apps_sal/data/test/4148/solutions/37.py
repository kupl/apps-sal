A = int(input())
a = list(input())
s = ''
for i in a:

    k = (ord(i) + A - 65) % 26
    s += chr(k + 65)
    # print(i,k,chr(k))

print(s)
