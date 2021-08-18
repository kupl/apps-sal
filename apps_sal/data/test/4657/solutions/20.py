'''input
3
2 1
1 1
5 4
1 2 3 4 5
6 2
1 2 8 4 10 2
'''
from copy import deepcopy
from bisect import bisect_right
from itertools import combinations
from sys import stdin


def dis(first, second, remain):
    if second[0] > first[0]:
        first[0], second[0] = second[0], first[0]

    if remain > first[0] - second[0]:
        remain -= first[0] - second[0]
        second[0] = first[0]
        first[0] += remain // 2
        return first[0]
    else:
        return second[0] + remain


q = int(stdin.readline().strip())
for _ in range(q):
    n, k = list(map(int, stdin.readline().split()))
    arr = list(map(int, stdin.readline().split()))
    temp = 0
    count = 0
    i = 0
    ans = []
    while i < len(arr) and count < k - 1:
        temp += arr[i]
        if temp % 2 == 1:
            ans.append(i + 1)
            temp = 0
            count += 1
        i += 1
    if len(ans) == 0:
        if sum(arr) % 2 == 1 and k == 1:
            print("YES")
            print(n)
        else:
            print("NO")

    elif sum(arr[ans[-1]:]) % 2 == 1:
        ans.append(n)
        count += 1
        if count == k:
            print("YES")
            print(*ans)
        else:
            print("NO")
    else:
        print("NO")
