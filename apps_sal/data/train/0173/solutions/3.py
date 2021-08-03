class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            return False
        import collections
        ans = []
        lookup = collections.defaultdict(list)
        for i, num in enumerate(arr):
            if (num % k) in lookup:
                ans.append((arr[lookup[(num % k)].pop(0)], num))
                if lookup[num % k] == []:
                    del lookup[num % k]
                continue
            if num % k == 0:
                lookup[0].append(i)
            else:
                lookup[(k - (num % k))].append(i)
        return len(ans) == len(arr) // 2
