n = int(input())
F = list(map(int, input().split()))
S = list(map(int, input().split()))

Sum = [0] * n
Sum[n - 1] = F[n - 1] + S[n - 1];

for i in range(n - 2, -1, -1):
    Sum[i] = Sum[i + 1] + F[i] + S[i]

ans1 = 0
for i in range(n):
    ans1 += F[i] * i;
    ans1 += S[i] * (2 * n - i - 1)

ans2 = 0
for i in range(n):
    ans2 += S[i] * (i + 1);
for i in range(1, n):
    ans2 += F[i] * (2 * n - i)

x = ans1
y = ans2
ans = [x, y]


for i in range(0, max(0, n - 2), 2):
    x = x + F[i + 1] * 2 - S[i] * (2 * n - 2 - 2 * i) - S[i + 1] * (2 * n - 4 - 2 * i) + Sum[i + 2] * 2
    y = y - F[i + 1] * (2 * n - 2 * i - 4) - F[i + 2] * (2 * n - 2 * i - 4) + Sum[i + 2] * 2
    ans.append(x)
    ans.append(y)


print(max(ans))
