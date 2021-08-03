class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # using bucket
        bucket = [None] * (len(s) + 1)
        hash_table = {}
        result = ''
        for item in s:
            hash_table[item] = hash_table.get(item, 0) + 1
        for key, value in hash_table.items():
            if bucket[value]:
                bucket[value].append((key, value))
            else:
                bucket[value] = [(key, value)]
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for item in bucket[i]:
                    result += item[0] * item[1]
        return result
