import sys
input = sys.stdin.readline

n, x = list(map(int, input().split()))

if n == x == 1:
    print(0)
    return


ANS = []
for i in range(n):
    if i + 1 == (x).bit_length():
        continue
    ANS = ANS + [(1 << i)] + ANS

print(len(ANS))
print(*ANS)
