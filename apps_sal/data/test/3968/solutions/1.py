from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

counter = Counter(A)

if counter[1] == 0 or counter[2] == 0:
    print(*A)
    return

if counter[1] == 1:
    ANS = [2, 1]
    ANS += [2] * (counter[2] - 1)
    print(*ANS)
    return

if counter[1] % 2 == 0:
    ANS = [2, 1]
    counter[2] -= 1
    counter[1] -= 1

    ANS += [1] * (counter[1] - 1)
    ANS += [2] * counter[2]
    ANS += [1]

    print(*ANS)
    return

if counter[1] % 2 == 1:
    ANS = [2, 1]
    counter[2] -= 1
    counter[1] -= 1

    ANS += [1] * counter[1]
    ANS += [2] * counter[2]

    print(*ANS)
    return
