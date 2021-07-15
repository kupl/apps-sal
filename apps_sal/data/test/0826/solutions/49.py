from decimal import Decimal
n=int(input())


# i=0
# while True:
#     i += 1
#     if i*(i+1)//2 <= n+1:
#         pass
#     else:
#         i -= 1
#         break


i = int((-1 + Decimal(1+8*(n+1)).sqrt())/2 )

print(n-i+1)        
