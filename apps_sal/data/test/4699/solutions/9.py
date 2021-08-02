n, k = input().split()
l = list(map(int, input().split()))
checkNum = [i for i in range(11)]


def find(x):
    while x != checkNum[x]:
        checkNum[x] = checkNum[checkNum[x]]
        x = checkNum[x]
    return x


for i in l:
    checkNum[find(i)] = checkNum[find(i + 1)]

fin = ""
for i in range(len(n)):
    first = int(n[i])
    k = find(first)
    if k == first:
        fin += str(k)
    else:
        if k != 10:
            fin = str(k) + str(find(0)) * (len(n) - i - 1)
        else:
            fin = str(find(1)) + str(find(0)) * len(n)
        break

print(fin)
