import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
res = 'no'
for start in range(n):
    for l in range(1, n):
        for j in range(start, start + l * 5, l):
            if j >= n:
                break
            if s[j] == '.':
                break
            if j == start + l * 4:
                res = 'yes'
print(res)
