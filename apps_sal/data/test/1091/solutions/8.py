'''
    CodeForces problem 386A
    26/01/2014
'''

# (x, y) = (offerta, tizio)
n = int( input() )
l = [ int(x) for x in input().split()]
i=1
off = []
for x in l:
    off.append( (x, i) )
    i+=1
    
off.sort( reverse=True )    

print(str(off[0][1])+' '+str(off[1][0]))

