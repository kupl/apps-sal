import math
##sa2=input().split(' ')
##candies=int(sa2[1])
##sa22=input().split(' ')
##sa3=[int(x) for x in sa22]
##
##def do(x, candies):
##    c2=[]
##    for element in x:
##        if element>candies:
##            c2.append(element-candies)
##
##    return c2
##
##while len(do(sa3, candies))>0:
##    sa3=do(sa3, candies)
##

sa2=input().split(' ')
candies=int(sa2[1])
sa22=input().split(' ')
sa3=[int(x) for x in sa22]

sa4=[]
for element in sa3:
    sa4.append(math.ceil(element/candies))
sa4.reverse()
print(int(sa2[0])-sa4.index(max(sa4)))

