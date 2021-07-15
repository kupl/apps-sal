N = int(input())
A = list(map(int, input().split()))

from collections import Counter

def check(counter, A):
    return len(counter) != len(A)

def Main(N, A):
    counter = Counter(A)
    lenC = len(counter)
    remains = N-lenC
    if remains%2 == 0:
        return lenC
    else:
        return lenC-1
    
          
print(Main(N, A))
