def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

def choose(n, k):
    c = 1
    if k > n // 2:
        k = n - k
    for i in range(1, k + 1):
        c = c * (n - i + 1) // i
    return c

def modulo(n):
    return n % (10 ** 9 + 7)

class Solution:
    
    def numWays(self, s: str) -> int:
        n = len(s)
        c = s.count('1')
        if c % 3 != 0:
            return 0
        cp = c // 3 # count in each part
        if cp == 0:
            #special case, no 1, chosse 2 separators in the (n-1) possible spaces
            return modulo(choose(n - 1, 2))
        # find the size n1 of the substring between (cp+1)-th and cp-th occurrances of 1,
        # and the size n2 of the subsring betwwen (cp*2+1)-th and (cp*2)-th occurrances of 1
        indices = list(findall('1', s))
        n1 = indices[cp] - indices[cp - 1] - 1
        n2 = indices[cp*2] - indices[cp*2 - 1] - 1
        # find one separater in (n1 + 1) possible spaces, 
        # and one separater in (n2 + 1) possible spaces 
        result = 0
        if n1 == 0:
            result = n2 + 1
        elif n2 == 0:
            result = n1 + 1
        else:
            result = (n1 + 1) * (n2 + 1)
        return(modulo(result))

