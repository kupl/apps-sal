n, s = list(map(int, input().split()))
u = list(map(int, input().split()))
mu = min(u)
su = sum(u)
if su < s:
    print(-1)
else:
    s -= (su - mu * n)
    if s <= 0:
        print(mu)
    else:
        k = s // n
        if s % n != 0:
            k += 1
        print(mu - k)
