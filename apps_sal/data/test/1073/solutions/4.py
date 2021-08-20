DIR = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
try:
    while True:
        n = int(input())
        s = input()
        result = 0
        for i in range(len(s)):
            y = x = 0
            for c in s[i:]:
                t = DIR[c]
                y += t[0]
                x += t[1]
                if y == x == 0:
                    result += 1
        print(result)
except EOFError:
    pass
