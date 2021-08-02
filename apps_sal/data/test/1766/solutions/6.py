n = int(input())
s1 = 0
s2 = 0
a = list(map(int, input().split()))
r = n - 1
l = 0
k = 0
for i in range(n):
    if a[l] > a[r]:
        if k == 0:
            s1 += a[l]
            k = 1
        else:
            s2 += a[l]
            k = 0
        l += 1

    else:
        if k == 0:
            s1 += a[r]
            k = 1
        else:
            s2 += a[r]
            k = 0
        r -= 1
print(s1, s2)
