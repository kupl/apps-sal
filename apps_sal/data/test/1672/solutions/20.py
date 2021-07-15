__author__ = 'Catherine'
n = int(input())
a = [-1]
ans = 1
j = 0
for i in range(n):
    m = input()
    a.append(int(m[0]))
    if a[j + 1] == a[j]:
        ans += 1
    a.append(int(m[1]))
    j += 2
print(ans)
