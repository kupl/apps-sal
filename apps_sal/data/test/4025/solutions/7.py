E = [0, 1, 2, 0, 2, 1, 0]
a = list(map(int, input().split()))
ans = 0
for d in range(7):
    e = E[d:] + E[:d]
    b = a.copy()
    pas = min(a[0] // 3, a[1] // 2, a[2] // 2)
    b[0] -= pas * 3
    b[1] -= pas * 2
    b[2] -= pas * 2
    it = 0
    while b[e[it]]:
        b[e[it]] -= 1
        it += 1
    ans = max(ans, pas * 7 + it)
print(ans)
