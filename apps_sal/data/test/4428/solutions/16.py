def R():
    return map(int, input().split())


n = int(input())
a = list(R())
ans = 0
i = 0
j = n - 1
s1 = 0
s3 = 0
while i < j:
    if s1 + a[i] == s3 + a[j]:
        s1 += a[i]
        s3 += a[j]
        i += 1
        j -= 1
        ans = s1
    elif s1 + a[i] < s3 + a[j]:
        s1 += a[i]
        i += 1
    else:
        s3 += a[j]
        j -= 1
print(ans)
