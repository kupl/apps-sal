class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        cache = Counter(A)
        c_list = sorted(list(cache), key=abs)
        for x in c_list:
            if cache[x] > cache[2 * x]:
                return False
            cache[2 * x] -= cache[x]
        return True
        '\n        if not A:\n            return True\n        positive_heap = []\n        negative_heap = []\n        zero = 0\n        positive_d = defaultdict(int)\n        negative_d = defaultdict(int)\n        for i in A:\n            if i == 0:\n                zero += 1\n            elif i < 0:\n                heappush(negative_heap, -i)\n                negative_d[-i] += 1\n            else:\n                heappush(positive_heap, i)\n                positive_d[i] += 1\n        if zero % 2 != 0:\n            return False\n        if not self.check(positive_heap, positive_d):\n            return False\n        if not self.check(negative_heap, negative_d):\n            return False\n        return True\n    \n    def check(self, h, d):\n        for _ in range(len(h)):\n            i = heappop(h)\n            if d[i] == 0:\n                continue\n            if 2*i not in d:\n                return False\n            elif d[2*i] < d[i]:\n                return False\n            else:\n                d[2*i] -= d[i]\n                d[i] = 0\n        return True\n    '
