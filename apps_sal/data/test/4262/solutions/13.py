import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
a = [i + 1 for i in range(N)]
x = 0
y = 0
i = 0
for b in itertools.permutations(a):
    if list(b) == P:
        x = i
    if list(b) == Q:
        y = i
    i += 1
print((abs(x - y)))
