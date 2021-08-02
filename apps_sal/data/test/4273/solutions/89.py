N = int(input())
d = {}
l = "MARCH"
c = [0 for _ in range(5)]
for n in range(N):
    S = input()
    for n in range(len(l)):
        if l[n] == S[0]:
            c[n] += 1
ans = 0
for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += c[i] * c[j] * c[k]
print(ans)
