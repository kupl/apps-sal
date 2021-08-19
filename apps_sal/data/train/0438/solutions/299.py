class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr) + 1
        group = [i for i in range(n)]
        bits = [False] * n
        root_to_size = [0] * n

        size_count = collections.defaultdict(int)
        size_count[0] = n
        ans = -1
        for step, num in enumerate(arr, start=1):
            g1 = self.find(group, num)
            bits[num] = True

            size_count[root_to_size[g1]] -= 1
            root_to_size[g1] += 1
            size_count[root_to_size[g1]] += 1

            if num + 1 <= len(arr) and bits[num + 1]:
                g2 = self.find(group, num + 1)
                group[g2] = g1
                combined_size = root_to_size[g1] + root_to_size[g2]
                size_count[root_to_size[g1]] -= 1
                size_count[root_to_size[g2]] -= 1
                root_to_size[g1] = combined_size
                size_count[root_to_size[g1]] += 1

            if num - 1 >= 1 and bits[num - 1]:
                g2 = self.find(group, num - 1)
                group[g2] = g1
                combined_size = root_to_size[g1] + root_to_size[g2]
                size_count[root_to_size[g1]] -= 1
                size_count[root_to_size[g2]] -= 1
                root_to_size[g1] = combined_size
                size_count[root_to_size[g1]] += 1

            if m in size_count and size_count[m] > 0:
                ans = step
            # print(ans, step, size_count)
        return ans

    def find(self, group, i):
        while group[i] != i:
            group[i] = group[group[i]]
            i = group[i]
        return i
