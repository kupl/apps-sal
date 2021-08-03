import sys
input = sys.stdin.readline
for f in range(int(input())):
    n, k = list(map(int, input().split()))
    sm = k // n
    bg = sm
    toad = k % n
    if toad != 0:
        bg += 1
    print(2 * (bg - sm)**2)
    for i in range(n):
        line = ""
        for j in range(n):
            x = i + j
            x %= n
            if x <= sm:
                if x < sm or i < toad:
                    line += "1"
                else:
                    line += "0"
            else:
                line += "0"
        print(line)
