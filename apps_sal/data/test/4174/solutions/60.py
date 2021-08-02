import bisect
N, X = list(map(int, input().split()))
L = list(map(int, input().split()))
List = [0] * (N + 1)
for i in range(1, N + 1):
    List[i] = List[i - 1] + L[i - 1]
# A = [i for i in List if i <=X]
# print(len(A))
print((bisect.bisect_left(List, X + 1)))
