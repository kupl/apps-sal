import sys
from collections import defaultdict


class BIT_RSQ(object):
    __slots__ = ['nodes', 'size']

    def __init__(self, size: int):
        self.nodes = [0]*(size+1)
        self.size = size+1

    def add(self, index: int, value: int):
        while index < self.size:
            self.nodes[index] += value
            index += index & -index

    def sum(self, right: int):
        result = 0

        while right:
            result += self.nodes[right]
            right -= right & -right

        return result


n = int(input())
a = list(map(int, input().split()))
bit = BIT_RSQ(n+10)
remove = defaultdict(list)
ans = 0

for i, x in enumerate(a, start=1):
    ans += bit.sum(min(i, x))
    if i < x:
        bit.add(i, 1)
        remove[min(n+1, x)].append(i)
    for j in remove[i]:
        bit.add(j, -1)

print(ans)

