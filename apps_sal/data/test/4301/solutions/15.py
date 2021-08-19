import heapq
n = int(input())
A = [int(input()) for _ in range(n)]
(m1, m2) = heapq.nlargest(2, A)
print(*[m2 if a == m1 else m1 for a in A], sep='\n')
