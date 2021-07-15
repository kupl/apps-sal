3

n = input()
v = list(map(int, input().split()))
v = v[::-1]
v.append(0)
v = v[::-1]
v.append(91)

sol = 90
for i in range(0, len(v)-1):
    if v[i] + 15 < v[i+1]:
        sol = v[i]+15
        break

sol = min(sol, 90)
print(sol)

