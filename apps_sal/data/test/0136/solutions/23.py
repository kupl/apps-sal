s=input()
s1=input()

if len(s)>len(s1):
       s1='0'*(len(s)-len(s1))+s1
else : 
        s='0'*(len(s1)-len(s))+s



if(s>s1):
    print('>')
elif(s<s1):
    print ('<')
else:
    print ('=')
