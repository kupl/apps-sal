
amount, balance=list(map(float,input().strip().split()))
if balance>=amount+0.50 and amount%5==0 and amount!=0:
    final=balance-amount-0.5
    print("{0:.2f}".format(final))

else:
    print("{0:.2f}".format(balance))

#a,b = map(float,input().strip().split())
#if a%5==0 and b>=a+0.50:
 #   print("{:.2f}".format(b-a-0.50))
#else:
 #   print("{:.2f}".format(b))

