n = int(input())
ui = list(map(int,input().split()))
ar = [0] * 100001
ar2 = [0] * 100001
maxi = 1
mini = 1
ans = 1
for i in range(n):
    if ar[ui[i]] == 0:
        ar[ui[i]] = 1
        mini = 1
        ar2[1] += 1
    else:
        ar2[ar[ui[i]]] -= 1
        if ar2[ar[ui[i]]] == 0 and mini == ar[ui[i]]:
            mini += 1
        ar[ui[i]] += 1
        ar2[ar[ui[i]]] += 1
    maxi = max(maxi,ar[ui[i]])
    if (maxi == mini and mini == 1) or mini == i + 1:
        ans = i + 1
    elif maxi == mini + 1 and ar2[maxi] == 1:
        ans = i + 1
    elif mini == 1 and ar2[maxi] * maxi == i:
        ans = i + 1
    if ar2[maxi] * maxi == i+1:
        if i != n - 1:
            ans = i + 2
print(ans)

