from math import factorial
(n, a, b) = list(map(int, input().split()))
v = list(map(int, input().split()))
v.sort(reverse=True)
ans = sum(v[:a]) / a
ans2 = 0
count1 = v.count(v[a - 1])
index1 = v.index(v[a - 1])


def ncr(x, y):
    return factorial(x) // factorial(y) // factorial(x - y)


if v[0] == v[a - 1]:
    for i in range(a, min(b, count1) + 1):
        ans2 += ncr(count1, i)
else:
    ans2 = ncr(count1, a - index1)
print(ans)
print(ans2)
