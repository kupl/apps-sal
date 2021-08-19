(n, k) = map(int, input().split())
f = list(map(int, input().split()))
f.sort(reverse=True)
ans = 0
places = 0
for fl in f:
    places += 1
    if places == 1:
        ans += 2 * (fl - 1)
    if places == k:
        places = 0
print(ans)
