n, k = list(map(int, input().split()))
s = input()
a = [0]
for i in range(n):
    if (s[i] == "0") == (len(a) % 2 == 1):
        a.append(1)
    else:
        a[-1] += 1
t = [0]
for i in a:
    t.append(i + t[-1])
ans = 0
for i in range(len(t)):
    if i % 2 == 0:
        # print(min(i + 2 * k + 1, len(t) - 1))
        ans = max(ans, t[min(i + 2 * k + 1, len(t) - 1)] - t[i])
print(ans)

