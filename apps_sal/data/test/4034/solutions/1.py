n = int(input())
s = input()
najm = [0] * n
najm[n-1] = s[n-1]
for i in range(n-1):
    j = n - i - 2
    najm[j] = min(najm[j+1], s[j+1])
can_sort = True
for i in range(n):
    for j in range(i+1, n-1):
        if s[i] > s[j] and s[j] > najm[j]:
            can_sort = False
            break
if not can_sort:
    print("NO")
else:
    print("YES")
    kol = [-1] * n
    kol[0] = 0
    ind = 0
    while ind < n:
        if kol[ind] == -1:
            kol[ind] = 0
        for i in range(ind+1,n):
            if s[i] < s[ind]:
                kol[i] = (kol[ind]+1)%2
        ind += 1
    print("".join(map(str,kol)))
