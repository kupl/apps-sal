from collections import defaultdict
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7


H, W, N = map(int, input().split())

dic = defaultdict(int)
lst = [0] * (10)
lst[0] = (H - 2) * (W - 2)

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 2 <= (a + i) <= (H - 1):
                if 2 <= (b + j) <= (W - 1):
                    tmp = dic[(a + i, b + j)]
                    lst[tmp] -= 1
                    lst[tmp + 1] += 1
                    dic[((a + i, b + j))] += 1

print(*lst, sep='\n')
