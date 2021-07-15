import sys

y = 0
x = 0
for i in range(5):
    in_str = (sys.stdin.readline()).split()
    for j in range(5):
        if(in_str[j] == '1'):
            x = j
            y = i
            print(abs(2 - x) + abs(2 - y))
            return
