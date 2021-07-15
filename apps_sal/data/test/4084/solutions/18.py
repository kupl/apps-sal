n = input()
n = n.split()
a = int(n[1])
b = int(n[2])
n = int(n[0])
if n%(a+b)<a:
    print(int(n/(a+b))*a+n%(a+b))
else:
    print(int(n/(a+b))*a+a)
