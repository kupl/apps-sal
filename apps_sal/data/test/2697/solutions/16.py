# cook your dish her
start = 1
c=0
end = int(input())
l=[] 
for val in range(start, end + 1): 
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           c+=1
          # l.append(val)
print(c)
