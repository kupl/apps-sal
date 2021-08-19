class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        A = [abs(num) for num in A]
        A.sort()
        dic = collections.defaultdict(collections.deque)
        for (i, num) in enumerate(A):
            dic[num].append(i)
        visited = [0] * len(A)
        cnt = 0
        i = 0
        while i < len(A):
            if visited[i]:
                i += 1
                continue
            (val, val_double) = (A[i], 2 * A[i])
            if val_double in dic and dic[val_double]:
                if val not in dic or not dic[val]:
                    return False
                dic[val].popleft()
                if not dic[val_double]:
                    return False
                index = dic[val_double].popleft()
                visited[index] = 1
            else:
                return False
            i += 1
        return True
