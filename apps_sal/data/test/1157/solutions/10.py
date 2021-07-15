n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = arr[i] // abs(arr[i])
pref = [1]
for i in range(n):
    pref.append(pref[-1] * arr[i])
plus = minus = 0
res_pl = res_mn = 0
for i in range(n + 1):
    if pref[i] == 1:
        res_pl += plus
        res_mn += minus
        plus += 1
    else:
        res_pl += minus
        res_mn += plus
        minus += 1
print(res_mn, res_pl)

