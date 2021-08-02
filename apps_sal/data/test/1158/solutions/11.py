pr = list([0 for x in range(101)])
n, k = list(map(int, input().split()))
inp = list(map(int, input().split()))
for i in inp:
    pr[i] += 1
pr.sort(reverse=True)
m = pr[0] // k + bool(pr[0] % k)
m *= k
ans = 0
i = 0
while i <= 100 and pr[i] > 0:
    ans = ans + m - pr[i]
    i += 1
print(ans)
