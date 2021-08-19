def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(input())
ans = n
c = 0
pre = ""
for i in range(n):
    s = bin((1 << n) + int(input(), 16))[3:]
    if i == 0 or s != pre:
        pre = s
        ans = gcd(ans, c)
        # print("c",c,"ans",ans)
        c = 1
        cc = 1
        for j in range(1, n):
            if s[j] == s[j - 1]:
                cc += 1
            else:
                ans = gcd(ans, cc)
                # print("cc",cc,"ans",ans)
                cc = 1

    else:
        c += 1

ans = gcd(ans, c)
# print(s)
print(ans)
