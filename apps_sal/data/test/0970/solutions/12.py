n = int(input())
p = list(sorted(map(int, input().split())))
s1 = s2 = 0
for i in range(n // 2):
    k = 1 + i * 2
    s1 += abs(p[i] - k)
    s2 += abs(p[i] - k - 1)
print(min(s1, s2))
