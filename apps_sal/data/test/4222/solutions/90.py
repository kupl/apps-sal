n, k = map(int, input().split())
ans = [1] + [0] * n
for i in range(k):
    d = int(input())
    l = list(map(int, input().split()))
    for i in l:
        ans[i] = 1
print(ans.count(0))
