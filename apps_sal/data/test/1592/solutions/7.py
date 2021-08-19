n = int(input())
ct = 0
cq = 0
mcq = 0
for i in range(n):
    (t, c) = list(map(int, input().split()))
    mcq = max(cq, mcq)
    cq = max(cq - (t - ct), 0)
    cq += c
    ct = t
mcq = max(cq, mcq)
ct += cq
print(ct, mcq)
