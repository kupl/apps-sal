import sys
import itertools
import functools

def brute_exact(n, k):
    ar = list(range(1, n + 1))
    combinations = list(itertools.combinations(ar, k))
    if not combinations:
        return 0
    
    xor_conv = lambda ar: functools.reduce(lambda x,y : x^y, ar)
    return max([xor_conv(combination) for combination in combinations]) 

def brute_atleast(n, k):
    return max([brute_exact(n, i) for i in range(1, k + 1)])

def solve(n, k):
    if k == 1:
        return n
    
    return 2**(n.bit_length()) - 1

def main():
    n, k = list(map(int, input().split()))
    print(solve(n, k))
	
def __starting_point():
    main() 
    

__starting_point()
