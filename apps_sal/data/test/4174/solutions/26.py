import bisect

N, X = list(map(int, input().split()))
L = list(map(int, input().split()))

D = [0]
for i in range(len(L)):
    D.append(sum(L[:i + 1]))
print((bisect.bisect_right(D, X)))
