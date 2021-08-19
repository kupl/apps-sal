class Solution:

    def numberOfSubarrays(self, A: List[int], B: int) -> int:
        import collections
        (q, k, temp, count) = (collections.deque(), 0, 0, 0)
        if B == 0:
            for i in range(len(A)):
                if A[i] % 2 == 0:
                    temp = temp + 1
                elif A[i] % 2 != 0:
                    count = count + int(temp * (temp + 1) / 2)
                    temp = 0
            count = count + int(temp * (temp + 1) / 2)
            return count
        while len(q) < B and k < len(A):
            if A[k] % 2 == 0:
                temp = temp + 1
            elif A[k] % 2 == 1:
                q.append(temp)
                temp = 0
            k = k + 1
        if len(q) < B:
            return 0
        temp = 0
        for i in range(k, len(A)):
            if A[i] % 2 == 0:
                temp = temp + 1
            elif A[i] % 2 != 0:
                count = count + (q[0] + 1) * (temp + 1)
                q.append(temp)
                q.popleft()
                temp = 0
        count = count + (q[0] + 1) * (temp + 1)
        return count
