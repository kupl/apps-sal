# n = list(map(int,unput().split()))
def print_lst(lst):
    print(" ".join(map(str,lst)))

n,k,p,x,y = list(map(int,input().split()))
pi = list(map(int,input().split())) 

spi = sum(pi)
res = []
c_lm = 0
c_hm = 0
for el in pi:
    if el < y:
        c_lm += 1
    else:
        c_hm += 1
n_hm = n//2+1 - c_hm
n_lm = n//2 -  c_lm
for i in range(n-k):
    
    if n_hm > 0:
        res += [y]
        pi += [y]
        n_hm -= 1
    elif n_lm > 0:
        res += [1]
        pi += [1]
        n_lm -= 1

pis = sorted(pi)
if sum(pis) > x:
    print(-1)
elif pis[len(pis)//2] < y:
    print(-1)
else:
    print_lst(res)


