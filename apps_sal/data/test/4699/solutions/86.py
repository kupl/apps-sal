n,t = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]

def check(x) -> bool:
    while x>0:
        a = x%10
        if a in d:
            return False
        x//=10
    return True

while check(n)==False:
    n+=1
print(n)
