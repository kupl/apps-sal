N = int(input())
A = sorted(list([int(x)-1 for x in input().split()]))
A = list([x-A[0] for x in A])
bucket = [0]*6010
for a in A: bucket[a] += 1
ans = 0
for i in range(6000):
    if bucket[i] > 1:
        ans += bucket[i] - 1
        bucket[i+1] += bucket[i] - 1
print(ans)

