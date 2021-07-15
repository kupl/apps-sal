N,M,K = list(map(int,input().split()))
B = list(map(int,input().split()))

seq = 1
intervals = []
for a,b in zip(B,B[1:]):
    if b-a == 1: continue
    intervals.append(b-a-1)
    seq += 1

if seq <= K:
    print(N)
    return

intervals.sort()
ans = N + sum(intervals[:seq-K])
print(ans)

