import heapq

n, m, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

a, b = heapq.nlargest(2, arr)

nb = m // (k + 1)
na = m - nb

h = na * a + nb * b
print(h)
