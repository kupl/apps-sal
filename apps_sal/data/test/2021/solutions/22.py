n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
a.sort(reverse=True)
pref = [0]
for i in range(n):
    pref.append(pref[i] + a[i])
for elem in q:
    ans = 0
    ans += pref[elem - 1]
    ans += pref[-1] - pref[elem]
    print(ans)
