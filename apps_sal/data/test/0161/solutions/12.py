x = int(input())
x = format(x, "b")
x = list(x)


ans = 0
anslist = []
for i in range(len(x)):
    if x[i] == "1":
        continue
    else:
        ans += 1
        anslist.append(len(x) - i)
        for j in range(i, len(x)):
            if x[j] == "1":
                x[j] = "0"
            else:
                x[j] = "1"

    if x.count("1") == len(x):
        break
    else:
        ans += 1
        x = "".join(x)
        x = int(x, 2)
        x += 1
        x = format(x, "b")
        x = list(x)

print(ans)
if len(anslist) != 0:
    print(" ".join(map(str, anslist)))
