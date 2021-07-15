import re
n = int( input() )
r1 = re.compile('^miao\..*lala\.$')
r2 = re.compile('lala\.$')
r3 = re.compile('^miao\.')

for i in range( 0, n ):
    s = str(input())
    #res1 = r1.findall( s ) )
    #res2 = r2.findall( s ) )
    if len( r1.findall( s ) ) > 0:
        print( 'OMG>.< I don\'t know!' )
    elif len( r2.findall( s ) ) > 0 :
        print( 'Freda\'s' )
    elif len( r3.findall( s ) ) > 0 :
        print ('Rainbow\'s')
    else:
        print( 'OMG>.< I don\'t know!' )

