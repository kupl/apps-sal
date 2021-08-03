def i3(): return map(int, input().split())


N, K = i3()
*D, = i3()

D = set(D)

for i in range(N, 10**5):
    ans = 1
    for s in str(i):
        if int(s) in D:
            ans = 0
            break
    if ans:
        break
print(i)
