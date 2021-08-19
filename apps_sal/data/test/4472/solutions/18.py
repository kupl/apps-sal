n = int(input())
a = input()
b = input()
ans = 0
if n % 2 != 0 and a[n // 2] != b[n // 2]:
    ans = 1
for i in range(n // 2):
    s = [a[i], b[i], a[n - i - 1], b[n - i - 1]]
    d = dict()
    for j in s:
        if d.get(j):
            d[j] += 1
        else:
            d[j] = 1
    if list(d.values()) != [2, 2] and list(d.values()) != [4]:
        if list(d.values()) == [1, 1, 1, 1]:
            ans += 2
            continue
        if a[i] == a[n - i - 1]:
            if list(d.values()) == [3, 1]:
                ans += 1
            else:
                ans += 2
            continue
        if b[i] == b[n - i - 1]:
            ans += 1
            continue
        ans += 1
print(ans)
