
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

n =  1000000000+7
a, b, c = map(int, input().split())
if(c==-1 and ((b%2==0 and a%2==1)or (b%2==1 and a%2==0))):
    print("0")
else :
    print(fastExpMod(2,(a-1)*(b-1),n))
