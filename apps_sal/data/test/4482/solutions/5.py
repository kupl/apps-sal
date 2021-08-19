n = int(input())
a = list(map(int, input().split()))
a_u = round(sum(a) / n)
a_d = int(sum(a) / n)
ans_u = 0
ans_d = 0
for i in range(n):
    ans_u += (a[i] - a_u) ** 2
    ans_d += (a[i] - a_d) ** 2
print(min(ans_u, ans_d))
