import sys
import math


def ii():
    return sys.stdin.readline().strip()


def idata():
    return [int(x) for x in ii().split()]


def bfs(graph1, root1):
    visited1 = set()
    queue1 = [[root1, 0]]
    visited1.add(root1)
    qw, ver = 0, 1
    while queue1:
        vertex1 = queue1[0]
        queue1 = queue1[1:]
        for neig1 in graph1[vertex1[0]]:
            if neig1 not in visited1:
                visited1.add(neig1)
                queue1 += [[neig1, vertex1[1] + 1]]
                if qw < vertex1[1] + 1:
                    ver, qw = neig1, vertex1[1] + 1
    return ver, qw


def dfs(graph, ver):
    used_v = set()
    depth = [0] * (len(graph) + 1)
    level = [ver]
    num_of_level = 0
    while level:
        new_level = []
        for v in level:
            depth[v] = num_of_level
            used_v.add(v)
            for v1 in graph[v]:
                if v1 not in used_v:
                    new_level += [v1]
        level = new_level
        num_of_level += 1
    return depth


def binary_search(array, x):
    left, right = -1, len(array)
    while left + 1 != right:
        middle = (left + right) // 2
        if array[middle] >= x:
            right = middle
        elif array[middle] < x:
            left = middle
    return right


def c_mod(n1, k1, mod1):
    num = den = 1
    for i in range(n1 - k1):
        num = (num * (n1 - i)) % mod1
        den = (den * (i + 1)) % mod1
    return (num * pow(den, mod1 - 2, mod1)) % mod1


def c(n1, k1):
    num = den = 1
    for i in range(n1 - k1):
        num = num * (n1 - i)
        den = den * (i + 1)
    return num // den


def v_sistemu(x, k):
    x = int(x)
    z = ''
    while x:
        z += str(x % k)
        x //= k
    return z[::-1]


def iz_sistemi(x, k):
    x = str(x)[::-1]
    ans = 0
    for i in range(len(x)):
        ans += int(x[i]) * pow(k, i)
    return ans


def solve_of_problem():
    n = int(ii())
    ans = 2
    for i in range(n):
        ans *= 2
        if n % (ans - 1) == 0:
            print(n // (ans - 1))
            return
    return


for ______ in range(int(ii())):
    solve_of_problem()
