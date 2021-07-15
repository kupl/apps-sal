dishes = [int(input()) for i in range(5)] 

d = [abs(d % 10 -10) for d in dishes if d % 10 != 0] # select nums which can be divided by 10
if d: d.remove(max(d)) 
print(sum(dishes) + sum(d))
