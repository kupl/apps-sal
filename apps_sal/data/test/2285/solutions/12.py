n = int(input())
ips = [input() for j in range(n)]
for ip in ips:
    if ip.find('::') != -1:
        ip = ip.replace('::', ':' * (9 - ip.count(':')))
    comps = ip.split(':')
    for i in range(len(comps)):
        comps[i] = '0' * (4 - len(comps[i])) + comps[i]
    print(':'.join(comps))
