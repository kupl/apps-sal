import bisect
(N, X) = list(map(int, input().split()))
L = list(map(int, input().split()))
List = [0] * (N + 1)
for i in range(1, N + 1):
    List[i] = List[i - 1] + L[i - 1]
print(bisect.bisect_left(List, X + 1))
