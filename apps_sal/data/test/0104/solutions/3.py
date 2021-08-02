n = int(input())

xs = [int(x) for x in input().split()]

ss = sum(xs)

s = 0
for i in range(n):
    s += xs[i]
    if s * 2 >= ss:
        print(i + 1)
        break
