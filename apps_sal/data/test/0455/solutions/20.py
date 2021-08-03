n = int(input())
x = [0 for i in range(0, n)]
y = [0 for i in range(0, n)]

for i in range(0, n):
    x[i], y[i] = [int(i) for i in input().split(" ")]

mod2 = (x[0] + y[0]) % 2
imp = False

for i in range(1, n):
    if (x[i] + y[i]) % 2 != mod2:
        print(-1)
        imp = True
        break

if not imp:
    if mod2 == 0:
        x = [i + 1 for i in x]

    u = [x[i] + y[i] for i in range(0, n)]
    v = [x[i] - y[i] for i in range(0, n)]

    mode = ["L", "D", "U", "R"]
    m = 31

    if mod2 == 0:
        print(m + 1)
        print("1 " + " ".join([str(2**(i - 1)) for i in range(1, m + 1)]))
    else:
        print(m)
        print(" ".join([str(2**(i - 1)) for i in range(1, m + 1)]))

    for i in range(0, n):
        w = ""
        if mod2 == 0:
            w = "L"
        ui = (u[i] + 2**m - 1) // 2
        vi = (v[i] + 2**m - 1) // 2
        for l in range(0, m):
            ul = ui % 2
            ui = ui // 2
            vl = vi % 2
            vi = vi // 2
            w += mode[ul * 2 + vl]
        print(w)
