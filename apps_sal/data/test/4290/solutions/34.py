import math
import sys
##### graph implementation with adjacancy list#####


class Graph:
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if self.is_directed == False:
            self.adj_list[v].append(u)

    def print_graph(self):
        for node in self.nodes:
            print((node, "->", self.adj_list[node]))

    def degree_node(self, node):
        return len(self.adj_list[node])

    def dfsUTIL(self, v, visited, parents=[]):
        #print(v,end=" ")
        visited[v] = True
        for i in self.adj_list[v]:
            if visited[i] == False:
                self.dfsUTIL(i, visited, parents)
                parents.append(i)

    def dfs(self, v):
        visited = [False] * (max(self.adj_list) + 1)
        parents = [v]
        self.dfsUTIL(v, visited, parents)
        return len(parents)

#####sorting a dictionary by the values#####


def dict_sort(ans):
    ans = sorted(list(ans.items()), reverse=True, key=lambda kv: (kv[1]))

##### naive method for testing prime or not O(n^.5)#####


def is_prime(n):
    if n == 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#####swap function#####


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

#####Primes till Nth O(n)#####


def seive_primes(n):
    flag = [0] * (n + 10)
    flag[1] = flag[0] = 1
    i = 2
    while i * i <= n + 1:
        if flag[i] == 0:
            j = i * i
            while j <= n + 1:
                flag[j] = 1
                j += i
        i += 1
    return flag

#####all the prime factors of a number#####


def factors(n):
    d = {}
    while(n % 2 == 0):
        if 2 in d:
            d[2] += 1
        else:
            d[2] = 1
        n /= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while(n % i == 0):
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            n /= i
    n = int(n)
    if n > 1:
        d[n] = 1
    return d

#####greatest common divisor of two numbers#####


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

#####least common multiplyer of two numbers#####


def lcm(a, b):
    return (a * b) // gcd(a, b)

#####function that return all the letters#####


def alphabates():
    return "abcdefghijklmnopqrstuvwxyz"

#####binary search O(logN)#####


def binary_search(ls, n, flag):
    low = 0
    hi = n - 1
    while(low <= hi):
        mid = (low + hi) // 2
        if ls[mid] == flag:
            return mid
        elif ls[mid] > flag:
            hi = mid - 1
        else:
            low = mid + 1
    return -1

#####quadratic roots#####


def qdrt(a, b, c):
    chk = b * b - 4 * a * c
    if chk >= 0:
        ans1 = (-b + chk**0.5) / (2 * a)
        ans2 = (-b - chk**0.5) / (2 * a)
        return [int(ans1), int(ans2)]
    return -1
#####permutations#####


def permutation(n, r):
    if n < r:
        return 0
    ans = 1
    for i in range(n - r + 1, n + 1):
        ans *= i
    return ans

#####combinations#####


def combination(n, r):
    if n < r:
        return 0
    ans = 1
    for i in range(r):
        ans *= (n - i)
    div = 1
    for i in range(2, r + 1):
        div *= i
    return ans // div

#####taking an array/list as input#####


def arinp():
    ls = list(map(int, input().split()))
    return ls

#####taking multiple inputs#####


def mult_inp():
    return list(map(int, input().split()))

#####Main function starts from here#####


def main():
    n, m = mult_inp()
    print((combination(n, 2) + combination(m, 2)))


def __starting_point():
    main()


__starting_point()
