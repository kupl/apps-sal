n, k = list(map(int, input().split()))
c = list(map(int, input().split()))
s = set(map(int, input().split()))
sust = sum(c)
su = 0
for i in s:
    sust -= c[i - 1]
    su += c[i - 1] * sust
for i in range(n):
    if (i + 1 not in s) and ((i + 1) % n + 1 not in s):
        su += c[i] * c[(i + 1) % n]
print(su)
