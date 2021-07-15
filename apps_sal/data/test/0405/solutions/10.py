n = int(input())
l = input()
ans = 0
for i in range(n):
    if l[i] == '<':
        ans += 1
    else:
        break
for i in range(n - 1, -1, -1):
    if l[i] == '>':
        ans += 1
    else:
        break
print(ans)

