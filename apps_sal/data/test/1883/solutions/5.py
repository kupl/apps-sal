import sys

def solve():
    n = int(input())
    types = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res = list()
    count = [0] * (n + 1)
    for val in a:
        count[val-1]+=1
    for i in range(n):
        if types[i] == 1:
            temp = list()
            cur = i
            while True:
                if count[cur] > 1 or cur < 0: break
                temp.append(cur + 1)
                cur = a[cur] - 1
            if len(temp) > len(res):
                res = temp
    print(len(res))
    return ' '.join(map(str, res[::-1]))
    # adj = [list() for _ in range(n)]
    # visited = [0] * (n + 1)
    # best = -1
    # start = -1
    # bestlen = 0
    # for i in range(n):
    #     if a[i] > 0: adj[a[i] - 1].append(i)
    # # counter = 0
    # for i in range(n):
    #     if visited[i] == 0:
    #         cur = i
    #         # temp = list()
    #         # temp.append(cur)
    #         temp = 1
    #         visited[cur] += 1
    #         while len(adj[cur]) == 1:
    #             # print(cur)
    #             if len(adj[cur]) > 0 and adj[cur][0] == cur: break
    #             cur = adj[cur][0]
    #             # temp.append(cur)
    #             visited[cur]+=1
    #             temp+=1
    #             # if counter == 10000: return - 1
    #         if types[cur] == 1 and temp > bestlen:
    #             best = cur
    #             bestlen = temp
    #             start = i
    # res = list()
    # while True:
    #     res.append(best)
    #     if best == start: break
    #     next = a[best] - 1
    #     best = next
    # res = res[::-1]
    # for i in range(len(res)): res[i] += 1
    # print(len(res))
    # return ' '.join(map(str, res))

if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
print(solve())
