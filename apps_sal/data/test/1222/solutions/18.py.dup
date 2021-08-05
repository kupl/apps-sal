import bisect

k = int(input())


def runrun(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if abs(int(str_n[i]) - int(str_n[i + 1])) > 1:
            return False
    return True


def build_runrun(d):
    r = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ans = []
    for i in r:
        if i == "0":
            continue
        queue = [[i, 1, i]]
        while queue != []:
            q = queue.pop(0)
            if q[1] > d:
                continue
            if q[1] == d:
                bisect.insort(ans, int(q[2]))
                continue

            queue.append([q[0], q[1] + 1, q[2] + q[0]])

            low = int(q[0]) - 1
            if low >= 0:
                queue.append([str(low), q[1] + 1, q[2] + str(low)])
            high = int(q[0]) + 1
            if high < 10:
                queue.append([str(high), q[1] + 1, q[2] + str(high)])

    return ans


run = []
d = 1
while len(run) < k:
    run.extend(build_runrun(d))
    d += 1

print((run[k - 1]))
