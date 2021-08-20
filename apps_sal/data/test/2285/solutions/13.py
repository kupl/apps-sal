for i in range(int(input())):
    ipv6 = input().split(':')
    ipv6 = [(4 - len(i)) * '0' + i if i != '' else '' for i in ipv6]
    if ipv6[-1] == '':
        ipv6[-1] = '0000'
    if ipv6[0] == '':
        ipv6[0] = '0000'
    if '' in ipv6:
        string = '0000:' * (8 - len(ipv6) + 1)
        ipv6[ipv6.index('')] = string[:-1]
    if '' in ipv6:
        ipv6.remove('')
    print(':'.join(ipv6))
