import sys


def get_max_kvazi(n):
    s = str(n)
    ans = ''
    for c in s:
        if c == '0':
            ans = ans + '0'
        else:
            ans = ans + '1'
    return int(ans)


fin = sys.stdin
fout = sys.stdout


n = int(fin.readline())
ans = []
while (n > 0):
    cur = get_max_kvazi(n)
    ans.append(cur)
    n -= cur
print(len(ans))
print(*ans)
