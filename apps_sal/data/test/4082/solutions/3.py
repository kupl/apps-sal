n = int(input())
l = list(map(int, input().split()))
end = [1]
for i in range(1, n):
    if l[i] > l[i - 1]:
        end.append(end[-1] + 1)
    else:
        end.append(1)
strt = [1] * n
for i in range(n - 2, -1, -1):
    if l[i] < l[i + 1]:
        strt[i] = strt[i + 1] + 1
    else:
        strt[i] = 1
ans = max(max(end), max(strt))
for i in range(1, n - 1):
    if l[i + 1] > l[i - 1]:
        ans = max(ans, end[i - 1] + strt[i + 1])
print(ans)
