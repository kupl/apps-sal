class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
            the arr's length is even
            each pair has two numbers
            get the remainder of each number divided by k
        '''
        n = len(arr)
        for i in range(n):
            arr[i] = arr[i] % k
        lookup = defaultdict(int)
        for i in range(n):
            if not arr[i]:
                continue
            if k - arr[i] in lookup:
                lookup[k - arr[i]] -= 1
                if not lookup[k - arr[i]]:
                    lookup.pop(k - arr[i])
            else:
                lookup[arr[i]] += 1

        if not lookup:
            return True
        return False
