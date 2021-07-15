n = int(input())

d = { x : [] for x in range(1, n + 1)}#defaultdict(list)
for x in range(n - 1):
    s,de = map(int, input().split())
    d[s].append(de)
    d[de].append(s)

def dfs():
    lst = [(0, 1.0, 1)]
    visited = set({1})
    ans = 0

    while lst:
        depth,prob,source = lst.pop()
        
        for neigh in d[source]:
            if neigh not in visited:
                visited.add(neigh)
                lst.append((depth + 1, prob*(1/(len(d[source]) - (1 if depth != 0 else 0))), neigh))
        
        if depth != 0 and len(d[source]) == 1:
            ans += prob*depth

    return ans

print("{:.8f}".format(dfs()))
