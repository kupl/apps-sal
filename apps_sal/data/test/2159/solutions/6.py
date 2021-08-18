'''l=0
r=10**13
while l+1<r:
    mid=(l+r)//2
    val=(max(0,b_b*mid-b)*rb+max(0,b_s*mid-s)*rs+max(0,b_c*mid-b)*rc)
    if val>money:
        r=mid
    if val<=money:
        l=mid'''
n = int(input())
arr = [int(q) - 1 for q in input().split()]
ans = [0] * n
for i in range(n):
    cnt = [0] * n
    best = 0
    for j in arr[i:]:
        cnt[j] += 1
        if cnt[j] > cnt[best] or j < best and cnt[j] == cnt[best]:
            best = j
        ans[best] += 1

print(*ans)
