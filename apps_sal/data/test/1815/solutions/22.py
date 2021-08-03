N = int(input())
arr = [int(x) for x in input().split()]
cnt = dict()
brr = set()
crr = [0 for _ in range(100001)]
for i in range(1, N + 1):
    cnt[i] = set()
answer = 1
for i in range(N):
    u = arr[i]
    crr[u] += 1
    if crr[u] > 1:
        cnt[crr[u] - 1].remove(u)
        if len(cnt[crr[u] - 1]) == 0:
            brr.remove(crr[u] - 1)
    cnt[crr[u]].add(u)
    brr.add(crr[u])
    if len(brr) == 1:
        drr = list(brr)
        if drr[0] == 1 or len(cnt[drr[0]]) == 1:
            answer = i + 1
    elif len(brr) == 2:
        drr = list(brr)
        drr.sort()
        if drr[0] == 1 and len(cnt[1]) == 1:
            answer = i + 1
        elif drr[1] == drr[0] + 1 and len(cnt[drr[1]]) == 1:
            answer = i + 1
print(answer)
