from functools import reduce

dominoes = [list([int(x) % 2 for x in input().split()]) for x in range(int(input()))]
temp1, temp2 = reduce(lambda a, x: (a + x[0]) % 2, dominoes, 0), reduce(lambda a, x: (a + x[1]) % 2, dominoes, 0)
if temp1 == temp2 == 0:
    print(0)
elif temp1 == temp2 == 1 and ([1, 0] in dominoes or [0, 1] in dominoes):
    print(1)
else:
    print(-1)
