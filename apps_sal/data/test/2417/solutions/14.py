ans = 0
d = {}
ans = 0
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = n - 1
j = n - 1
d = {}
while i >= 0:
    if a[i] == b[j]:
        i -= 1
        j -= 1
    else:
        d[a[i]] = 1
        if b[j] not in d:
            i -= 1
            ans += 1
        else:
            j -= 1
print(ans)
