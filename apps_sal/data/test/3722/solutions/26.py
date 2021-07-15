n = int(input())
c = [input() for _ in range(4)]

mod = 10**9+7

const = [['A', 'A', 'A', 'A'],
['A', 'A', 'A', 'B'],
['A', 'A', 'B', 'A'],
['A', 'A', 'B', 'B'],
['A', 'B', 'A', 'B'],
['A', 'B', 'B', 'B'],
['B', 'B', 'A', 'B'],
['B', 'B', 'B', 'B']]

if c in const:
    print(1)
    return

exps = [['A', 'B', 'A', 'A'],
['B', 'A', 'B', 'A'],
['B', 'A', 'B', 'B'],
['B', 'B', 'A', 'A']]

if c in exps:
    print(pow(2,max(n-3,0),mod))
    return

def fib(n,acm1=1,acm2=1):
    if not n:
        return acm2
    return fib(n-1,acm2,acm1+acm2)
print(fib(max(n-3,0))%mod)
