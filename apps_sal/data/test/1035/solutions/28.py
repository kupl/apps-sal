import math
#試し割法
def trial_division(n):
    #素因数を格納するリスト
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    #リストが空ならそれは素数
    if not factor:
        factor.append(1)
        factor.append(n)
        return factor
    else:
        factor.append(1)
        factor.append(n)
        return factor
A,B=list(map(int,input().split()))
A_primes=trial_division(A)
B_primes=trial_division(B)
primes=[]
for p in A_primes:
  if p in B_primes:
    primes.append(B_primes.pop(B_primes.index(p)))
print((len(list(set(primes)))))

