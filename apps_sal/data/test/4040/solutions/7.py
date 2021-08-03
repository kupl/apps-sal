data = (list(map(int, input().split())))

c = (list(map(int, input().split())))

csum = sum(c)

if (data[2] == 0):
    print("NO")
else:
    if (csum + (data[2] - 1) * (data[1] + 1) >= data[0]):
        print("YES")

        empt = data[0] - csum

        allempt = 0

        sol = []

        for i in range(data[1]):

            if(allempt < empt):
                for z in range(data[2] - 1):
                    if(allempt >= empt):
                        break
                    sol.append(0)
                    allempt += 1

            for j in range(c[i]):
                sol.append((i + 1))

            q = data[0] - len(sol)

        if (q != 0):
            for i in range(q):
                sol.append(0)

        print(*sol)

    else:
        print("NO")
