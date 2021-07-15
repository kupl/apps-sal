import fractions

a,b,c,d = map(int, input().split())

def t(tar, l1, l2):
    return (tar - (tar//l1 + tar//l2) + tar//(l1*l2//(fractions.gcd(l1, l2))))

print(t(b,c,d) - t(a-1,c,d))
