import itertools
n = int(input())
m = list("MARCH")
d = [0] * 5
for i in range(n):
    s = input()
    for j in range(len(m)):
        if s[0] == m[j]:
            d[j] += 1
ans = 0
for i in list(itertools.combinations(list(range(5)), 3)):
    k = list(i)
    ans += d[k[0]] * d[k[1]] * d[k[2]]
print(ans)
