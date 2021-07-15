import sys

T = int(sys.stdin.readline())
for t in range (0, T):
    n, a, b = list(map(int, sys.stdin.readline().strip().split()))
    s = sys.stdin.readline().strip()
    i = 0
    c = n * a + (n + 1) * b
    v = 0
    for j in range (0, n-1):
        if s[j] == "1" or s[j+1] == "1":
            c = c + b
            v = 1
    if v == 1:
        c = c + 2 * a
        while s[i] == "0":
            i = i + 1
        j = n - 1
        while s[j] == "0":
            j = j - 1
        v = 0
        while i <= j:
            if s[i] == "1":
                if v > 0:
                    c = c + min([(v-1) * b, 2 * a])
                v = 0
            if s[i] == "0":
                v = v + 1
            i = i + 1
    print(c)

            

