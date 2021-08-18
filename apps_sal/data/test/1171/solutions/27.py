import bisect
import sys
input = sys.stdin.readline
N, K = (int(i) for i in input().split())
V = list(map(int, input().split()))
V_sorted = sorted(V)


ans = []
take_V = []
if V_sorted[-1] <= 0:
    ans = 0
else:
    take_num = min(K, N)
    for tak in range(1, take_num + 1):
        reverse = min(K - tak, tak)
        for lef in range(tak + 1):
            for rev in range(reverse + 1):

                take = []
                rig = N - (tak - lef)
                take.extend(V[:lef])
                take.extend(V[rig:])
                take.sort()
                take_V.append(sum(take[rev:]))

    ans = max(take_V)
print(ans)
