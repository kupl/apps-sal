input()
n = [int(x) for x in input().split()]
s = sum(n)
trgt = s // 2 + s % 2

for i, x in enumerate(n):
    trgt -= x
    if trgt <= 0:
        print(i + 1)
        break
