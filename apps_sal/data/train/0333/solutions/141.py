class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dp = {}
        count = {}
        for i in range(len(arr)):
            res = count.get(arr[i], [])
            res.append(i)
            count[arr[i]] = res

        vis = set()
        vis.add(0)
        q = collections.deque([(0, 0)])
        c = 0
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if node[0] == len(arr) - 1:
                    return node[1]

                if node[0] != 0:
                    if node[0] - 1 not in vis:
                        q.append((node[0] - 1, node[1] + 1))
                        vis.add(node[0] - 1)

                if node[0] != len(arr) - 1:
                    if node[0] + 1 not in vis:
                        q.append((node[0] + 1, node[1] + 1))
                        vis.add(node[0] + 1)

                for j in count[arr[node[0]]]:
                    if j not in vis and j != node[0]:
                        q.append((j, node[1] + 1))
                        vis.add(j)
                if j in count[arr[node[0]]]:
                    count[arr[node[0]]] = []

            c += 1
