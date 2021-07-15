chain = input()
pearls = chain.count('o')
elements = chain.count('-')
if pearls == 0:
    print ('YES')
elif (elements%pearls)==0:
    print ('YES')
else:
    print ('NO')

