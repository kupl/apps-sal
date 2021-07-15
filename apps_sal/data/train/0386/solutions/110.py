class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if not n:
            return 0

        dic = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        dp_cur = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1,
        }

        for i in range(1, n):
            dp_next = collections.defaultdict(int)
            for key, item in list(dp_cur.items()):
                for j in dic[key]:
                    dp_next[j] += item
            dp_cur = dp_next

        return sum(dp_cur.values()) % (10 ** 9 + 7)

