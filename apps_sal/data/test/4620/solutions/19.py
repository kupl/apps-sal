n = int(input())
c_s_f = []
for i in range(n - 1):
    line = list(map(int, input().split()))
    c_s_f.append(line)

for i in range(n - 1):
    t = c_s_f[i][0] + c_s_f[i][1]
    for j in range(i + 1, n - 1):
        if t <= c_s_f[j][1]:
            t = c_s_f[j][1] + c_s_f[j][0]
        else:
            t = (t + c_s_f[j][2] - 1) // c_s_f[j][2] * \
                c_s_f[j][2] + c_s_f[j][0]
    print(t)
print((0))
