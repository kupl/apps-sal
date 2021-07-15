password=input()
a=b=c=0
if len(password)>4:
    for i in password:
        if a==0 and (ord(i) in range(48,58)): a=1
        if b==0 and (ord(i) in range(65,91)): b=1
        if c==0 and (ord(i) in range(97,123)): c=1
        if a+b+c>2:
            print('Correct')
            return
print ('Too weak')


