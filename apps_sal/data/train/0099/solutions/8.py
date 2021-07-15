from sys import stdin, stdout
import math

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    st, end = float('inf'), -1
    for i in range(n):
        if s[i] == '1':
            st = i
            break

    for i in range(n-1, -1, -1):
        if s[i] == '0':
            end = i
            break

    if st < end:
        print(s[:st]+'0'+s[end+1:])
    else:
        print(s)



