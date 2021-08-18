n, k = map(int, input().split())
r, s, p = map(int, input().split())
read_data = input()

res = 0
log = []
for i in range(len(read_data)):
    if len(log) < k:
        if read_data[i] == 'r':
            res += p
        if read_data[i] == 's':
            res += r
        if read_data[i] == 'p':
            res += s

        log.append(read_data[i])

    else:
        tmp = log.pop(0)
        if tmp != read_data[i]:
            if read_data[i] == 'r':
                res += p
            if read_data[i] == 's':
                res += r
            if read_data[i] == 'p':
                res += s
            log.append(read_data[i])
        else:
            log.append('-')


print(res)
