k=input()
l = input()

a1=[]

for i in l:
    n=(ord(i)-65+(int)(k))%26+65
    a1.append(chr(n))
a1=''.join(a1)
print(a1)
