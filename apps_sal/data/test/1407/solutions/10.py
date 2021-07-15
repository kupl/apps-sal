#python3
import sys, threading, os.path
import collections, heapq, math,bisect
import string
from platform import python_version
import itertools
sys.setrecursionlimit(10**6)
threading.stack_size(2**27)     

def generate_primes(n):
    res = []
    isPrime = [True]*(n*5)
    isPrime[0],isPrime[1] = 0,0
    '''
    for (ll i = 2; i*i <= n+1; ++i) {
        if (isPrime[i]) {
            for (ll j = i * 2; j <= n; j += i)
                isPrime[j] = 0;
        }
    }
    '''
    for i in range(2,n+1):
        if i*i >n+1:
            break
        if isPrime[i]:
            for j in range(i*2,n+1,i):
                isPrime[j]=0

    res.append(2)
    for i in range(3,n+1,2):
        if isPrime[i]:
            res.append(i)
    return res;


def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    n,m = list(map(int, input.readline().split()))
    mat = []
    for i in range(n):
        mat.append(list(map(int, input.readline().split())))
    allprimes = generate_primes(150000)
    #print(allprimes)
    tostore = []
    for i in range(n):
        tostore.append([])
        for j in range(m):
            x = bisect.bisect(allprimes, mat[i][j])
            if allprimes[x-1]==mat[i][j]:
                tostore[i].append(0)
            else:
                tostore[i].append(abs(mat[i][j]-allprimes[x]))
    '''
    for i in range(n):
        for j in range(m):
            print(tostore[i][j], end=" ")
        print()
    ''' 
    
    rowsum,colsum = [0]*501,[0]*501
    for i in range(n):
        for j in range(m):
            rowsum[i]+=tostore[i][j]
            colsum[j]+=tostore[i][j]
    #print(rowsum[:n])
    #print(colsum[:m])
    minone = min(min(rowsum[:n]),min(colsum[:m]))    
    output = minone
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


def __starting_point():
    main()
#threading.Thread(target=main).start()

__starting_point()
