class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        # intuition: BFS
        dic = {}
        for i, num in enumerate(arr):
            if num not in dic:
                dic[num] = set()
            dic[num].add(i)

        bag = set(list(range(1, len(arr))))
        queue = [0]
        res = 0
        print(bag)
        while len(queue) > 0:
            l = len(queue)
            for _ in range(l):
                node = queue.pop(0)
                if node == len(arr) - 1:
                    return res
                # neighbors
                if node > 0:
                    if node - 1 in bag:
                        queue.append(node - 1)
                        bag.remove(node - 1)
                        if arr[node - 1] in dic and node - 1 in dic[arr[node - 1]]:
                            dic[arr[node - 1]].remove(node - 1)
                            if not dic[arr[node - 1]]:
                                del dic[arr[node - 1]]
                if node < len(arr) - 1:
                    if node + 1 in bag:
                        queue.append(node + 1)
                        bag.remove(node + 1)
                        if arr[node - 1] in dic and node - 1 in dic[arr[node - 1]]:
                            dic[arr[node - 1]].remove(node - 1)
                            if not dic[arr[node - 1]]:
                                del dic[arr[node - 1]]
                # SAME VALUE
                if arr[node] in dic:
                    for i in dic[arr[node]]:
                        if i in bag:
                            bag.remove(i)
                            queue.append(i)
                    del dic[arr[node]]
            res += 1
