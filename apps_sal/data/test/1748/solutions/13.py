def bin_search(pref, diff, s, val):
    e = len(pref) - 1
    index = -1
    while s <= e:
        mid = (s + e) >> 1
        if pref[mid] - diff <= val:
            index = mid
            s = mid + 1
        else:
            e = mid - 1
    return index


n = int(input())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
pref = [0 for i in range(len(t))]
pref[0] = t[0]
for i in range(1, len(t)):
    pref[i] = t[i] + pref[i - 1]

freq = [0 for i in range(len(t))]
ans = [0 for i in range(len(t))]
diff = 0

for i in range(0, n):
    index = bin_search(pref, diff, i, a[i])
    if index == -1:
        ans[i] += a[i]
    else:
        freq[i] += 1
        if index + 1 < n:
            freq[index + 1] -= 1
            ans[index + 1] += (a[i] - pref[index] + diff)
    diff += t[i]

for i in range(1, n):
    freq[i] = freq[i] + freq[i - 1]

for i in range(0, n):
    print(freq[i] * t[i] + ans[i], end=" ")
print()
