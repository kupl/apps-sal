problems = input().split()
c = int(problems[0])
d = int(problems[1])
n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
k = int(input())

t = n * m - k
ans = 100000000
i = 0
while i * n <= t:
    ans = min(ans, (t - i * n) * d + i * c)
    i += 1
ans = min(ans, i * c)
print(ans)
