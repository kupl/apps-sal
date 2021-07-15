from sys import stdin
inFile = stdin
tokens = []
tokens_next = 0

def next_str():
    nonlocal tokens, tokens_next
    while tokens_next >= len(tokens):
        tokens = inFile.readline().split()
        tokens_next = 0
    tokens_next += 1
    return tokens[tokens_next - 1]

def nextInt():
    return int(next_str())

from heapq import heapify, heappop
def min_cost(a, k):
    if k > len(a):
        return False

    new_a = [a[i] + (i + 1) * k for i in range(len(a))]
    heapify(new_a)
    s = 0
    for _ in range(k):
        s += heappop(new_a)
    return s

n = nextInt()
S = nextInt()
a = [nextInt() for _ in range(n)]

low = 0
high = n + 1
while low + 1 < high:
    mid = (low + high) // 2
    if min_cost(a, mid) <= S:
        low = mid
    else:
        high = mid

print(low, min_cost(a, low)) 
