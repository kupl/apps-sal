n = int(input())
a = list(map(int, input().split()))
mini = min(a)
s1 = a.index(mini)
s2 = 0
for i in range(s1 + 1, n):
    if(a[i] == mini):
        s2 = i
        break
ans = s2 - s1
for i in range(s2 + 1, n):
    if(a[i] == mini):
        ans = min(ans, i - s2)
        s1 = s2
        s2 = i
print(ans)
