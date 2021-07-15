jacket,socks,money=map(int,input().split())
money-=jacket
number_of_socks=money//socks
#print(number_of_socks,money,socks)
if number_of_socks%2==0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')
