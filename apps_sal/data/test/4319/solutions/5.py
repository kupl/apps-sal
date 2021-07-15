n = int(input())
s = [int(elem) for elem in input().split()]
ans = 0
anses = []
s.append(1)
for i in range(n):
    if s[i] >= s[i + 1]:
        ans = ans + 1
        anses.append(s[i])
print(ans)
for i in range(ans):
    print(anses[i],end=' ')
