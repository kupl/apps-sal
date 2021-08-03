class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        count = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        dic = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}

        for i in range(n - 1):
            tmp = {}
            for x in dic:
                for v in dic[x]:
                    tmp[v] = (tmp.get(v, 0) + count[x]) % mod
            count = tmp
        return sum(count.values()) % mod
