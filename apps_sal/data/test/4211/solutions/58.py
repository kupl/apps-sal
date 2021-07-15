# ABC 140 C
N = int(input())
B = [int(i) for i in input().split()]
ans = B[0] + B[-1]
if N >= 3:
    for i in range(0, N-2):
        ans += min(B[i], B[i+1])

print(ans)
