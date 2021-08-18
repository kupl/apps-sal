homename = input()
awayname = input()
fouls = int(input())

a = []
b = []
for foul in range(fouls):
    data = input().split()
    if data[3] == "r":
        for j in range(len(b)):
            if b[j][1:3] == data[1:3]:
                break
        else:
            if data[1] == "h":
                print(" ".join([homename, data[2], data[0]]))
            else:
                print(" ".join([awayname, data[2], data[0]]))
        b.append(data)
    else:

        for i in range(len(a)):
            if a[i][1:] == data[1:]:
                if data[1] == "h":
                    print(" ".join([homename, data[2], data[0]]))
                else:
                    print(" ".join([awayname, data[2], data[0]]))
                b.append(a[i])
                a.remove(a[i])

                break

        else:
            for j in range(len(b)):
                if b[j][1:3] == data[1:3]:
                    break
            else:
                a.append(data)
