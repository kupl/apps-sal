import sys
sys.setrecursionlimit(10 ** 9)  
import threading
threading.stack_size(67108864)
def main():
    n, m = [int(x) for x in input().split()]

    graph = []

    for i in range(n):
        graph.append([])

    deg = [0] * n

    for i in range(m):
        a, b = [int(x) - 1 for x in input().split()]
        deg[a] += 1
        deg[b] += 1
        graph[a].append(b)
        graph[b].append(a)

    used = [0] * n

    # print()
    def dfs(v):
        is_cir = 1
        if deg[v] != 2:
            is_cir = 0
        for child in graph[v]:
            if not used[child]:
                used[child] = 1
                is_cir = min(dfs(child), is_cir)
        return is_cir


    head = 0
    count = 0
    while 1:
        #print(used, head)
        used[head] = 1
        is_cir = dfs(head)
        count += is_cir
        f = 0
        for i in range(head, n):
            if not used[i]:
                head = i
                f = 1
                break
                
        if not f:
            print(count)
            return



thread = threading.Thread(target=main)
thread.start()
thread.join()
