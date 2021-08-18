n = int(input())
s = str(input())
left = s[0]
ans = 10**6
left = {}
left.setdefault('W', 0)
left.setdefault('E', 0)
right = {}
right.setdefault('E', 0)
right.setdefault('W', 0)
for i in range(n):
    right[s[i]] += 1
ans = 10**6
for i in range(n):
    right[s[i]] -= 1
    ans = min(ans, left['W'] + right['E'])
    left[s[i]] += 1
print(ans)
