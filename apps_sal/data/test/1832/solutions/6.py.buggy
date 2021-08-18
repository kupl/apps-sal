
# from math import factorial as fac
from collections import deque, defaultdict
from heapq import heapify, heappush, heappop
from types import GeneratorType
import heapq
import math
from collections import deque
from collections import defaultdict
# from copy import deepcopy
import sys
import math
f = None
try:
    f = open('q1.input', 'r')
except IOError:
    f = sys.stdin
if 'xrange' in dir(__builtins__):
    range = xrange
# print(f.readline())
# sys.setrecursionlimit(10**6)


def print_case_iterable(case_num, iterable):
    print("Case #{}: {}".format(case_num, " ".join(map(str, iterable))))


def print_case_number(case_num, iterable):
    print("Case #{}: {}".format(case_num, iterable))


def print_iterable(A):
    print(' '.join(A))


def read_int():
    return int(f.readline().strip())


def read_int_array():
    return [int(x) for x in f.readline().strip().split(" ")]


def rns():
    a = [x for x in f.readline().split(" ")]
    return int(a[0]), a[1].strip()


def read_string():
    return list(f.readline().strip())


def ri():
    return int(f.readline().strip())


def ria():
    return [int(x) for x in f.readline().strip().split(" ")]


def rns():
    a = [x for x in f.readline().split(" ")]
    return int(a[0]), a[1].strip()


def rs():
    return list(f.readline().strip())


def bi(x):
    return bin(x)[2:]


NUMBER = 10**9 + 7
# NUMBER = 998244353


def factorial(n):
    M = NUMBER
    f = 1

    for i in range(1, n + 1):
        f = (f * i) % M  # Now f never can
        # exceed 10^9+7
    return f


def mult(a, b):
    return (a * b) % NUMBER


def minus(a, b):
    return (a - b) % NUMBER


def plus(a, b):
    return (a + b) % NUMBER


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a):
    m = NUMBER
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def choose(n, k):
    if n < k:
        assert false
    return mult(factorial(n), modinv(mult(factorial(k), factorial(n - k)))) % NUMBER


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def dfs(g, timeIn, timeOut, depths, parents):
    # assign In-time to node u
    cnt = 0
    # node, neig_i, parent, depth
    stack = [[1, 0, 0, 0]]
    while stack:
        v, neig_i, parent, depth = stack[-1]
        parents[v] = parent
        depths[v] = depth
        # print (v)
        if neig_i == 0:
            timeIn[v] = cnt
            cnt += 1
        while neig_i < len(g[v]):
            u = g[v][neig_i]
            if u == parent:
                neig_i += 1
                continue
            stack[-1][1] = neig_i + 1
            stack.append([u, 0, v, depth + 1])
            break
        if neig_i == len(g[v]):
            stack.pop()
            timeOut[v] = cnt
            cnt += 1

# def isAncestor(u: int, v: int, timeIn: list, timeOut: list) -> str:
# 	return timeIn[u] <= timeIn[v] and timeOut[v] <= timeOut[u]


cnt = 0


@bootstrap
def dfs(v, adj, timeIn, timeOut, depths, parents, parent=0, depth=0):
    nonlocal cnt
    parents[v] = parent
    depths[v] = depth
    timeIn[v] = cnt
    cnt += 1
    for u in adj[v]:
        if u == parent:
            continue
        yield dfs(u, adj, timeIn, timeOut, depths, parents, v, depth + 1)
    timeOut[v] = cnt
    cnt += 1
    yield


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Function to return LCM of two numbers


def lcm(a, b):
    return (a * b) / gcd(a, b)


def get_num_2_5(n):
    twos = 0
    fives = 0
    while n > 0 and n % 2 == 0:
        n //= 2
        twos += 1
    while n > 0 and n % 5 == 0:
        n //= 5
        fives += 1
    return (twos, fives)


def shift(a, i, num):
    for _ in range(num):
        a[i], a[i + 1], a[i + 2] = a[i + 2], a[i], a[i + 1]


def equal(x, y):
    return abs(x - y) <= 1e-9
# def leq(x,y):
# 	return x-y <= 1e-9


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


def getLength(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def bfs(adj):
    s = set()
    d = defaultdict(set)
    # print('\n'.join(map(str,E.items())))
    q = deque([])
    s.add(0)
    d[0].add(0)
    q.append((0, 0))
    while len(q) > 0:
        v, depth = q.popleft()
        for u in adj[v]:
            if u not in s:
                s.add(u)
                d[depth + 1].add(u)
                q.append((u, depth + 1))
        # print(q)
    return d


@bootstrap
def dfs(u, top, adj, vis):
    vis[u] = 1
    for v, d in adj[u]:
        if vis[v] == 2 or d == 0:
            continue
        if vis[v] == 1:
            yield "No"
        x = yield dfs(v, top, adj, vis)
        if x == "No":
            yield "No"
    vis[u] = 2
    top.append(u)
    yield


def isSubsetSum(arr, n, summ):

    # The value of subarr[i][j] will be
    # true if there is a
    # subarr of arr[0..j-1] with summ equal to i
    subarr = ([[False for i in range(summ + 1)]
               for i in range(n + 1)])

    # If summ is 0, then answer is true
    for i in range(n + 1):
        subarr[i][0] = True

    # If summ is not 0 and arr is empty,
    # then answer is false
    for i in range(1, summ + 1):
        subarr[0][i] = False

    # Fill the subarr table in botton up manner
    for i in range(1, n + 1):
        for j in range(1, summ + 1):
            if j < arr[i - 1]:
                subarr[i][j] = subarr[i - 1][j]
            if j >= arr[i - 1]:
                subarr[i][j] = (subarr[i - 1][j] or
                                subarr[i - 1 ][j-arr[i-1]])

    # uncomment this code to print table
    # for i in range(n + 1):
    # for j in range(summ + 1):
    # print (subset[i][j], end =" ")
    # print()
    return subarr[n][summ]


def find_lcm(a, b):
    return (a * b) // gcd(a, b)


def find_lcm_array(A):
    if len(A) == 1:
        return A[0]
    lcm = find_lcm(A[0], A[1])

    for i in range(2, len(A)):
        lcm = find_lcm(lcm, A[i])
    return lcm


def solution(a, n):
    res = ['a' * 50]
    for i in range(n):
        x = a[i]
        if x == 50:
            res.append(res[-1])
            continue
        temp = res[-1]
        char = res[-1][x]
        char = 'a' if char == 'z' else 'z'
        res.append(temp[:x] + char + temp[x + 1:])
    return '\n'.join(res)


def main():
    T = 1
    T = ri()
    for i in range(T):
        n = ri()
        a = ria()
        # s = rs()
        # n,m,k	= ria()
        # adj = [list() for _ in range(n)]
        # for _ in range(m):
        # 	d,a,b=ria();
        # 	a-=1; b-=1
        # 	adj[a].append((b,d))
        # 	if d == 0:
        # 		adj[b].append((a,d))

        x = solution(a, n)

        # continue
        if 'xrange' not in dir(__builtins__):
            print(x)  # print("Case #"+str(i+1)+':',x)
        else:
            print >>output, "Case #" + str(i + 1) + ':', str(x)
    if 'xrange' in dir(__builtins__):
        print(output.getvalue())
        output.close()


if 'xrange' in dir(__builtins__):
    import cStringIO
    output = cStringIO.StringIO()
# example usage:
#    for l in res:
#       print >>output, str(len(l)) + ' ' +  ' '.join(l)


def __starting_point():
    main()


__starting_point()
