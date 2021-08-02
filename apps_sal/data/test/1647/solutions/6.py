def f(x):
    if data[x] != x:
        data[x] = f(data[x])
        return data[x]
    return x


n = int(input())
s = input()
t = input()
data = [i for i in range(26)]
for i in range(n):
    a, b = f(ord(s[i]) - ord("a")), f(ord(t[i]) - ord("a"))
    if a != b:
        data[a] = b
ans = 0
for i in range(26):
    f(i)
for i in range(26):
    ans += max(0, data.count(i) - 1)
print(ans)
for i in range(26):
    ans = []
    for j in range(26):
        if data[j] == i:
            ans.append(chr(j + ord("a")))
    for j in range(len(ans) - 1):
        print(ans[j], ans[j + 1])
