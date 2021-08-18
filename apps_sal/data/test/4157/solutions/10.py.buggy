import sys
n = int(input())
lis = list(map(int, input().split()))
for j in range(n):
    ans = []
    curr = lis[j]
    cnt = 0
    while cnt < n:
        ans.append(curr)
        cnt += 1
        if curr * 2 in lis:
            curr *= 2
        elif curr // 3 in lis and curr % 3 == 0:
            curr = curr // 3
        else:
            break
    if cnt == n:
        ans = [str(p) for p in ans]
        print(" ".join(ans))
        return
print(-1)
