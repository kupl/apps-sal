n = str(int(input())+1)
if n.count("0")+1 == len(n):
    print(1)
else:
    print((int(n[0])+1)*10**(len(n)-1)-int(n)+1)
    

