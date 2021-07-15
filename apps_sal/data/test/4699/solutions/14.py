N, K = map(int, input().split())
D = list(map(int, input().split()))


def f(n, x):
    if n==0:
        if x >= N:
            print(x)
            return
        return
    
    for i in range(10):
        if i in D:
            continue
        f(n-1, x*10+i)

f(len(str(N)), 0)
ans = ""
for i in range(1, 10):
    if i not in D:
        ans = str(i)
        break
for i in range(10):
    if i not in D:
        ans += str(i)*len(str(N))
        break
print(ans)
