from decimal import *
from math import sqrt,tan,pi

def __starting_point():

    getcontext().prec = 50

    l3,l4,l5 = map( Decimal , input().split() )
    #print(l3,l4,l5)

    S3 = Decimal(sqrt(3))*l3*l3/4
    H3 = Decimal(sqrt(6))*l3/3
    area3 = S3*H3/3

    S4 = l4*l4
    H4 = Decimal(sqrt(2))*l4/2
    area4 = S4*H4/3

    h5 = l5*Decimal(tan(54*pi/180))/2
    S5 = (l5*h5/2)*5
    H5 = Decimal(sqrt((3*l5*l5/4)-(h5*h5)))
    area5 = S5*H5/3

    res = area3 + area4 + area5

    print(res)
__starting_point()
