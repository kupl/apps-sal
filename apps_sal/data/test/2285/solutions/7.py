count = input()
for i in range(int(count)):
    n = input()
    ip = n.split(':')
    begin = 0
    end = 0
    if (ip[0] == '' and ip[1] == '' and len(ip) > 8):
        begin = 1
    if (ip[len(ip) - 2] == '' and ip[len(ip) - 1] == '' and len(ip) > 8):
        end = 1
    while len(ip) < 8:
        index = ip.index('')
        ip = ip[:index] + [''] + ip[index:]
    for item in ip:
        i = item
        while len(i) < 4:
            i = '0' + i
        ip[ip.index(item)] = i
    if end == 1:
        ip = ip[:len(ip) - 1]
    if begin == 1:
        ip = ip[1:]
    print(':'.join(ip))
