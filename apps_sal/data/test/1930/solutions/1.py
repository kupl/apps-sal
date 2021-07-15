n = int(input())

L = [int(x) for x in input().split()]
D = {}
J = []
S = []
T = [0]*(n+1)
for i in range(n):
    if L[i] > 0:
        D[L[i]] = i
        J.append(L[i])
        T[i+1] = T[i]
    else:
        T[i+1] = T[i]+1
        
def I(J):
    if len(J) <= 1:
        return J, 0
    else:
        a = J[:len(J)//2]
        b = J[len(J)//2:]
        a, ai = I(a)
        b, bi = I(b)
        c = []
        i = 0
        j = 0
        inversions = ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

for i in range(1,n+1):
    if not i in D:
        S.append(i)

total = len(S)
num = 1
denom = 1
if total > 0:
    themostimportantsum = 0
    for i in J:
        low = 0
        high = total-1
        while high-low > 1:
            guess = (high+low)//2
            if S[guess] > i:
                high = guess
            else:
                low = guess
        if S[low] > i:
            smaller = low
        elif S[high] > i:
            smaller = high
        else:
            smaller = high+1
        #D[i] is the position of i in the list
        #T[D[i]] is how many -1s there are to the left of it
        themostimportantsum += T[D[i]]*(total-smaller)+(total-T[D[i]])*(smaller)
        num = themostimportantsum+total
        denom = total

num =(denom*(((total)*(total-1))//2)+2*num)%998244353
denom *= 2
if num == denom:
    if I(J)[1] == 0:
        print(0)
    else:
        print(I(J)[1]%998244353)
else:       
    num += denom*I(J)[1]
    print(((num-denom)*pow(denom%998244353,998244351,998244353))%998244353)

