import sys

n, t = map(int, input().split())

s1 = input()
s2 = input()

same = sum([1 for i in range(n) if s1[i] ==s2[i]])

def other(c1, c2):
    ans = 'a'
    while ans == c1 or ans == c2:
        ans = chr(ord(ans) + 1)
    return ans

if same + 2 * t < n:
    print(-1)
    return

samehave = 0
sames1 = 0
sames2 = 0

ans = ['v'] * n

for i in range(n):
    if s1[i] == s2[i]:
        if sames1 < n - t and sames2 < n - t:
            ans[i] = s1[i]
            sames1 += 1
            sames2 += 1
        else:
            ans[i] = other(s1[i], s2[i])

for i in range(n):
    if s1[i] != s2[i]:
        if sames1 < n - t:
            sames1 += 1
            ans[i] = s1[i]
        elif sames2 < n - t:
            sames2 += 1
            ans[i] = s2[i]
        else:
            ans[i] = other(s1[i], s2[i])
        

print(*ans, sep='')
