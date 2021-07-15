import itertools as it

n = int(input())
k = 0
kar = map(int, input().split())
koy = map(int, input().split())
all = set(it.chain(kar, koy))
for i, j in it.product(kar, koy):
    if i ^ j in all:
        k += 1
print('Karen' if k % 2 == 0 else 'Koyomi')
