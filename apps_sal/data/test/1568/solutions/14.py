(n, a, b, c, T) = list(map(int, input().split()))
t = list(map(int, input().split()))
smth = [0] * T
for i in range(len(t)):
    smth[t[i] - 1] += 1
ans1 = 0
ans2 = 0
for i in range(len(t)):
    ans1 += a
k = 0
for i in range(T):
    ans2 += c * k
    k += smth[i]
for i in range(len(t)):
    ans2 += a - (T - t[i]) * b
print(max(ans1, ans2))
'k = 0\nfor i in range(len(smth)):\n    k += smth[i]\n    k -= 1'
