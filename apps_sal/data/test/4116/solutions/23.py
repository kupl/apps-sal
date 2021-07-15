N=int(input())
x="No"
for i in range(1,10):
    if N%i==0 and N/i<10:
       x="Yes"
       break
print(x) 
