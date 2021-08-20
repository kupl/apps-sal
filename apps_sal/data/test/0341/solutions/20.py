(n, k) = map(int, input().split())
(R, S, P) = map(int, input().split())
t = input()
v = {'r': P, 's': R, 'p': S}
ans = 0
for i in range(k):
    check = t[i]
    ans += v[check]
    while True:
        i += k
        if i >= n:
            break
        if check == t[i]:
            check = '-1'
        else:
            ans += v[t[i]]
            check = t[i]
print(ans)
