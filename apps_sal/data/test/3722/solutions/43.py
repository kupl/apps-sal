import sys
input = sys.stdin.readline
N = int(input())
mod = 10 ** 9 + 7
AA = input().strip()
AB = input().strip()
BA = input().strip()
BB = input().strip()
if (AA, AB, BA, BB) in {('A', 'A', 'A', 'A'), ('A', 'A', 'A', 'B'), ('A', 'A', 'B', 'A'), ('A', 'A', 'B', 'B'), ('A', 'B', 'A', 'B'), ('A', 'B', 'B', 'B'), ('B', 'B', 'A', 'B'), ('B', 'B', 'B', 'B')}:
    print(1)
elif (AA, AB, BA, BB) in {('A', 'B', 'A', 'A'), ('B', 'A', 'B', 'A'), ('B', 'A', 'B', 'B'), ('B', 'B', 'A', 'A')}:
    ANS = [0, 0, 1, 1, 2]
    for i in range(1000):
        ANS.append(ANS[-1] * 2 % mod)
    print(ANS[N])
elif (AA, AB, BA, BB) in {('A', 'B', 'B', 'A'), ('B', 'A', 'A', 'A'), ('B', 'A', 'A', 'B'), ('B', 'B', 'B', 'A')}:
    ANS = [0, 0, 1, 1, 2, 3, 5]
    for i in range(1000):
        ANS.append((ANS[-1] + ANS[-2]) % mod)
    print(ANS[N])
