from itertools import permutations
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
m = [set() for _ in range(27)]
for a, b in AB:
    m[a].add(b)
    m[b].add(a)

def main():
    ans = []
    def traverse(n, visits):
        visits = visits | set([n])
        if len(visits) == N:
            ans.append(1)
            return
        for c in m[n] - visits:
            traverse(c, visits)
    traverse(1, set())
    return len(ans)

print(main())
