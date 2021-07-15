import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    X = int(input())
    answer = 0
    pow2 = 1

    while True:
        r = 2**pow2 - 1
        needed = r*(r+1) // 2
        if needed <= X:
            answer += 1
            X -= needed
        else:
            break
        pow2 += 1

    print(answer)

