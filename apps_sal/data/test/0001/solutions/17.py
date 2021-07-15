n = int(input().strip())

s = []
while n > 0:
    s.append(n % 10)
    n //= 10
s = s[::-1]

n = len(s)
ans = 0
best = -1
for i in range(n):
    res = sum(s[:i + 1]) - 1 + 9 * (n - i - 1)
    if res >= ans:
        ans = res
        best = i

def get(s, pos):
    ans = 0
    for i in range(len(s)):
        if i > pos:
            ans = ans * 10 + 9
        else:
            ans = ans * 10 + s[i]
            if i == pos:
                ans -= 1
    return ans

if sum(s) >= ans:
    print(get(s, n))
else:
    print(get(s, best))


