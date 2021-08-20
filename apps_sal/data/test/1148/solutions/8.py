col = int(input())
ll = list(map(int, input().split()))
a1 = col * min(ll)
m = min(ll)
s = []
t = 0
for i in ll:
    t += 1
    if i == m:
        s.append(t - 1)
        t = 0
s[0] += t
print(a1 + max(s))
