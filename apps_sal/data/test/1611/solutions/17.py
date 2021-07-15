n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)

k = sum(l) / 3

ans = [0, 0, 0]
j = 0

for i in l:
    ans[j] += i
    if ans[j] >= k:
        j += 1

ans.sort(reverse=True)


print(ans[0] - ans[1] + 1 - ans[2])
