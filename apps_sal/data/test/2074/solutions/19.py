s=input().split()
n=int(s[0])
m=int(s[1])
town=[]
town = []
minpricestreet=[]
for i in range(n):
    row = input().split()
    for k in range(len(row)):
        row[k] = int(row[k])
    town.append(row)
    minpricestreet.append(min(row))
 
maxposprice=0
  
for i in (list(range(n))):
    if minpricestreet[i]>maxposprice:
        street_num=i
        maxposprice=minpricestreet[i]

price=min(town[street_num])
    
        
print(price)        

