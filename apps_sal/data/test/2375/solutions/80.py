a,b=list(map(int,input().split()))
cnt=1
if abs(a-b)<=1:
    print('Brown')
else:
    print('Alice')


# if b>a:
#     a,b=b,a
# a=a-b
# b=0
# mod_a=a%3
# if a==3:
#     print('Alice')
# elif mod_a==2:
#     print('Alice')
# elif mod_a==1:
#     print('Brown')
# elif (mod_a==0)and(a!=3):
#     print('Brown')
# if (mod_a==3)and(mod_b==3):
#     print('Alice')
# elif (mod_a==3)and(mod_b==1):
#     print('Alice')
# elif (mod_a==1)and(mod_b==3):
#     print('Alice')
# elif (mod_a==2)and(mod_b==0):
#     print('Alice')    
# elif (mod_a==0)and(mod_b==2):
#     print('Alice')
# else:
#     print('Brown')

