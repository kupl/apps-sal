n = int(input())
for i in range(n):
    r = input().split(':')
    s = ':'.join((x.zfill(4) if x else x for x in r))
    while len(s) < 39:
        x = s.index('::')
        s = s[:x + 1] + '0000:' + s[x + 1:]
    if '::' in s:
        x = s.index('::')
        s = s[:x + 1] + s[x + 2:]
    print(s.strip(':'))
