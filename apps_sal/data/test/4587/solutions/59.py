from bisect import bisect, bisect_left

N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

C_accum = [0]
for b in B:
    C_accum.append(C_accum[-1] + N - bisect(C, b))

ans = 0
for a in A:
    i = bisect(B, a)
    ans += C_accum[-1] - C_accum[i]

print(ans)
