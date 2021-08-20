n = int(input())
l = list(map(int, input().split()))
pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + l[i - 1]
q = int(input())
for i in range(q):
    (l, r) = list(map(int, input().split()))
    print((pref[r] - pref[l - 1]) // 10)
