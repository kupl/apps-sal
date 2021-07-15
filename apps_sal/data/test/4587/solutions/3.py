from bisect import bisect_left, bisect_right
N = int(input())
A, B, C = [sorted(map(int, input().split())) for _ in range(3)]
print(sum(bisect_left(A,b)*(N-bisect_right(C,b)) for b in B))
