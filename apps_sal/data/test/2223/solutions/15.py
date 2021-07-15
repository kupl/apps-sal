def main():
    n = int(input())
    if n % 2 != 0: print((-1)); return;

    graph = [[] for _ in range(n)]

    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    res = 0    
    stack = [0]
    visited = [-1] * n
    visited[0] = 0

    count = [1] * n

    while stack:
        s = stack[-1]
        flag = False

        for v in graph[s]:
            if visited[v] == -1:
                stack.append(v)
                visited[v] = s
                flag = True

        if not flag:
            stack.pop()
            if s == 0: break;
            count[visited[s]] += count[s]

    res = sum([1 if i % 2 == 0 else 0 for i in count])
    print(res-1)

def __starting_point():
    main()


__starting_point()
