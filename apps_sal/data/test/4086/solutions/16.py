n = int(input())
arr = list(map(int, input().split()))
d = {}
for i in range(n):
    d[arr[i]] = i
ans = []
for i in d.keys():
    ans.append([d[i], i])
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i][1], end=' ')
print('')
