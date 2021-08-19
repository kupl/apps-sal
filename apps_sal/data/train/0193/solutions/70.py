class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        arr_map = Counter(arr)
        arr_tup = [(item, arr_map[item]) for item in arr_map]
        arr_tup = sorted(arr_tup, key=lambda x: -x[1])
        count = 0
        total = 0
        for item in arr_tup:
            total += item[1]
            print(item[0])
            count += 1
            if total >= n / 2:
                return count
    ' n = len(arr)\n        \n        freq = {}\n        for i in arr:\n            if i in freq:\n                freq[i] += 1\n            else:\n                freq[i] = 1\n                \n        new_set = set()\n                \n        max_freq = max(freq, key = freq.get)\n        del(freq[max_freq])\n        \n        new_set.add(max_freq)\n        \n        arr = [val for val in arr if val != max_freq]\n        \n        while True:\n            \n            if len(arr) <= n//2:\n                return len(new_set)\n            else:\n                max_freq = max(freq, key = freq.get)\n                del(freq[max_freq])\n                new_set.add(max_freq)\n                arr = [val for val in arr if val != max_freq]'
