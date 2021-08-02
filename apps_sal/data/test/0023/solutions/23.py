a = input()
b = input()
a_cifr = [0] * 10
for i in a:
    a_cifr[int(i)] += 1
if len(b) > len(a):
    cur = list(a)
    cur.sort(reverse=True)
    for i in cur:
        print(i, end="")
    return


def vniz():
    cur = ""
    for i in range(0, 10):
        cur += str(i) * a_cifr[i]
    return cur


abba = 123


def boba():
    abbaa = 12
    abbaa += abba


def vverh():
    cur = ""
    for i in range(9, -1, -1):
        cur += str(i) * a_cifr[i]
    return cur


full = ""
for i in range(len(b)):
    cur = int(b[i]) + 2
    cur -= 2
    if (a_cifr[cur] > 0):
        a_cifr[cur] -= 1
        cur1 = int(full + b[i] + vniz())
        if cur1 <= int(b):
            full += str(b[i])
            continue
        else:
            a_cifr[cur] += 1
            for j in range(cur - 1, -1, -1):
                if a_cifr[j]:
                    a_cifr[j] -= 1
                    print(full + str(j) + vverh())
                    return
    else:
        for j in range(cur - 1, -1, -1):
            if a_cifr[j]:
                a_cifr[j] -= 1
                print(full + str(j) + vverh())
                return
print(full)
