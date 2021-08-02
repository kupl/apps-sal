n = int(input())
arr = list(map(int, input().split()))

ans = 0
pref = [0]
prefset = {0}
for i in range(n):
    now = pref[-1] + arr[i]
    if now in prefset:
        ans += 1
        pref = [0, arr[i]]
        prefset = {0, arr[i]}
    else:
        pref.append(now)
        prefset.add(now)
    # print(pref)
    # print(prefset)

print(ans)
