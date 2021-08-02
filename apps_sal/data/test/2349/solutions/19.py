import sys


# inf = open('input.txt', 'r')
# reader = (int(line.rstrip()) for line in inf)
reader = (int(s.rstrip()) for s in sys.stdin)


def rating(n):
    m = n
    ans = [0, 1]
    ndiv = 2
    while True:
        brick = n // ndiv
        if not brick:
            break
        ndiv = n // brick
        ans.append(ndiv)
        ndiv += 1
    return ans


t = next(reader)
for _ in range(t):
    n = next(reader)
    ans = rating(n)
    sys.stdout.write(str(len(ans)) + '\n')
    sys.stdout.write(' '.join(map(str, ans)) + '\n')

# inf.close()
