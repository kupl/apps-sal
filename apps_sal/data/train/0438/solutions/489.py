class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        '''
        length_dict = {}

        length_edge = [0]*len(arr)

        result = -1

        for i in range(len(arr)):
            index = arr[i] - 1

            left_length = 0
            right_length = 0
            if index>0:
                left_length = length_edge[index - 1]
            if index<len(arr)-1:
                right_length = length_edge[index + 1]
            length_edge[index+right_length] = 1 + left_length + right_length
            length_edge[index-left_length] = 1 + left_length + right_length

            if left_length in length_dict:
                length_dict[left_length] -= 1
            if right_length in length_dict:
                length_dict[right_length] -= 1
            if 1 + left_length + right_length not in length_dict:
                length_dict[1 + left_length + right_length] = 0
            length_dict[1 + left_length + right_length] += 1

            if m in length_dict and length_dict[m]>0:
                result = i + 1
        return result
        '''
        n, ans = len(arr), -1
        uf = UnionFindSet(n)

        groups = {}
        groups[0] = len(arr)

        result = -1
        for step, i in enumerate(arr):
            i -= 1
            uf.ranks[i] = 1

            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    '''
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    '''
                    groups[uf.ranks[uf.find(j)]] -= 1
                    if uf.ranks[j]:
                        uf.union(i, j)

            if uf.ranks[uf.find(i)] == m:
                ans = step + 1
            group = uf.ranks[uf.find(i)]
            if group not in groups:
                groups[group] = 0
            groups[group] += 1
            if m in groups and groups[m] > 0:
                result = step + 1
        '''
        for i in range(n):
            if uf.ranks[uf.find(i)] == m:
                return n
        return ans
        '''

        return result
