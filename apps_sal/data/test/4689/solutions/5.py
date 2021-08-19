(A, B) = map(int, input().split())
f = list(map(int, input().split()))
kyori = []
for i in range(len(f) - 1):
    an = f[i + 1] - f[i]
    kyori.append(an)
an2 = A - f[-1] + f[0]
ans = max(max(kyori), an2)
print(A - ans)
