N = int(input())
m = [0] * 5
s = "MARCH"
for i in range(N):
    a = input()
    for j in range(5):
        if s[j] == a[0]:
            m[j] += 1

ans = 0

for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += m[i] * m[j] * m[k]

print(ans)
