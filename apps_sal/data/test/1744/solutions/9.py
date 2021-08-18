
def main1():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    M = int(buflist[1])
    buf = input()
    buflist = buf.split()
    t = list(map(int, buflist))
    student = []
    minimum = []
    for i in range(n):
        count = 0
        pointer = 0
        while pointer < i:
            if count + student[pointer] <= M - t[i]:
                count += student[pointer]
                pointer += 1
            else:
                break
        minimum.append(i - pointer)
        student.append(t[i])
        student.sort()
    print(' '.join(list(map(str, minimum))))


def main2():
    buf = input()
    buflist = buf.split()
    n = int(buflist[0])
    M = int(buflist[1])
    buf = input()
    buflist = buf.split()
    t = list(map(int, buflist))
    bucket = []
    for i in range(101):
        bucket.append(0)
    minimum = []
    for i in range(n):
        target = M - t[i]
        count = 0
        subtotal = 0
        for j in range(1, 101):
            if subtotal + bucket[j] * j > target:
                count += (target - subtotal) // j
                break
            else:
                count += bucket[j]
                subtotal += bucket[j] * j
        minimum.append(i - count)
        bucket[t[i]] += 1
    print(' '.join(list(map(str, minimum))))


def __starting_point():
    main2()


__starting_point()
