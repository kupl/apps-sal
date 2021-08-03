n = int(input())
m = [0 for i in range(400)]
f = [0 for i in range(400)]
ppl = []
for i in range(n):
    tmp = input().split()
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    ppl.append(tmp)

ans = 0
for day in range(1, 367):
    for p in ppl:
        gender, a, b = p
        if a <= day <= b:
            if gender == 'M':
                m[day] += 1
            else:
                f[day] += 1
    ans = max(ans, min(m[day], f[day]))
print(2 * ans)
