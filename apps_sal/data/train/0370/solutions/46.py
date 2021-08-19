class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        graph = defaultdict(list)
        nodes = set(nums)
        roots = set()
        m, n = len(nums), max(nums)
        primes = [True] * (n + 1)
        for i in range(2, n // 2 + 1):
            if not primes[i]:
                continue
            j = i * 2
            while j <= n:
                primes[j] = False
                if j in nodes:
                    graph[i].append(j)
                    graph[j].append(i)
                    roots.add(i)
                j += i
        # print(graph)
        ans = self.traverse(graph, roots, nodes)
        # print(ans)
        return max(ans)

    def traverse(self, graph, roots, real_nodes):
        counts = []
        vztd = set()
        for node in roots:
            if node in vztd:
                continue
            cnt = 0
            vztd.add(node)
            q = [node]
            while q:
                next_q = []
                for n in q:
                    if n in real_nodes:
                        cnt += 1
                    for nab in graph[n]:
                        if nab not in vztd:
                            vztd.add(nab)
                            next_q.append(nab)
                q = next_q
            counts.append(cnt)
        return counts
