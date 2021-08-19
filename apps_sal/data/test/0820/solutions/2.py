n = int(input())
m = int(input())
v = []
for i in range(n):
    v.append(int(input()))
v = sorted(v)[::-1]
sol = 0
for i in range(0, len(v)):
    if m <= 0:
        break
    sol += 1
    m -= v[i]
print(sol)
