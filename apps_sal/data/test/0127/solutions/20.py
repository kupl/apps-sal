n, f = map(int, input(). split())
days = []
ans = 0
for i in range(n):
    k, l = map(int, input(). split())
    if(k < l):
        new_k = 2 * k
        if new_k >= l:
            days. append(k - l)
        else:
            days. append(-k)
        ans += k
    else:
        ans += l

days = sorted(days)

for i in range(min(f, len(days))):
    ans -= days[i]
print(ans)
