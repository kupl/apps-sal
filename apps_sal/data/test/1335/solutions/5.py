def r(x):
    return int(x + 0.50000000001)


n, k = list(map(int, input().split()))
arr = [int(x) for x in input().split()]
arr = arr[::-1]
sys = [[0, 0, n + 1] for _ in range(k)]
cnt = 0
done = 0
ints = [False] * n
s = len(arr)
c = 0

for i in range(10**8):

    tmp = 0

    for j in range(len(sys)):

        if sys[j][0] >= sys[j][1]:
            if arr:
                sys[j] = [0, arr.pop(), c]
                c += 1
            else:
                sys[j] = [0, 0, n + 1]
        sys[j][0] += 1

    q = r(100 * done / s)
    for j in range(len(sys)):
        if sys[j][1] == 0:
            tmp += 1
        if sys[j][0] == q and sys[j][1] >= sys[j][0]:
            ints[sys[j][2]] = True

    for j in range(len(sys)):
        if sys[j][1] != 0 and sys[j][0] >= sys[j][1]:
            done += 1

    if tmp == len(sys):
        break

d = 0
for i in ints:
    d += i
print(d)
