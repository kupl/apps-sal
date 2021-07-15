n = int(input())
arr = list(map(int, input().split()))
pref1 = [0]
for i in arr:
    pref1.append(pref1[-1] + i)
suf0 = [0]
for i in arr[::-1]:
    suf0.append(suf0[-1] + (i + 1) % 2)
ans = []
for i in range(n + 1):
    ans.append(n - (suf0[::-1][i] + pref1[i]))
print(max(ans))
