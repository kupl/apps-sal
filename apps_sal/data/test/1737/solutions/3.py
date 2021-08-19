from queue import Queue


def main():
    n = int(input())
    d = {}
    res = {}
    start = None
    for i in range(n):
        (project, version) = input().split()
        version = int(version)
        if i == 0:
            start = (project, version)
        k = int(input())
        if project not in d:
            d[project] = {}
        if version not in d[project]:
            d[project][version] = []
        for j in range(k):
            (p, v) = input().split()
            v = int(v)
            d[project][version].append((p, v))
        if i != n - 1:
            input()
    q = Queue()
    q.put(start)
    k = 1
    while not q.empty():
        append = {}
        for i in range(k):
            (s_p, s_v) = q.get()
            for (p, v) in d[s_p][s_v]:
                if p == start[0]:
                    continue
                if p in res:
                    continue
                if p not in append or append[p] < v:
                    append[p] = v
        k = len(append)
        for p in append:
            res[p] = append[p]
            q.put((p, append[p]))
    ans = []
    for p in res:
        v = res[p]
        ans.append((p, v))
    ans = sorted(ans, key=lambda z: z[0])
    print(len(ans))
    for (p, v) in ans:
        print(p, v)


main()
