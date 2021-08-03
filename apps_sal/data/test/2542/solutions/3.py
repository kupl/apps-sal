import math
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    s = input()[:-1]

    answer = math.inf
    for n1 in range(10):
        sn1 = str(n1)
        for n2 in range(10):
            sn2 = str(n2)
            lookn1 = True
            current = 0
            for c in s:
                if c == sn1 and lookn1:
                    lookn1 = False
                    current += 1
                elif c == sn2 and not lookn1:
                    lookn1 = True
                    current += 1
            if current % 2 and n1 != n2:
                current -= 1

            answer = min(answer, len(s) - current)

    print(answer)
