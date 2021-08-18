import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
a = list(map(lambda x: (x[0] - x[1], x[1]), enumerate(map(int, input().split()))))
s = {}
for i, v in a:
    if i in s:
        s[i] += v
    else:
        s[i] = v
print(max(s.values()))
