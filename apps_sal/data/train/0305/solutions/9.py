class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        echos = set()

        def find_echos(suffix):
            n = len(suffix)
            z = [0] * n
            (l, r) = (0, 0)
            for i in range(1, n):
                if r >= i:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and suffix[i + z[i]] == suffix[z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    (l, r) = (i, i + z[i] - 1)
            for half in range(1, 1 + n // 2):
                if z[half] >= half:
                    echos.add(suffix[:2 * half])
        for i in range(len(text) - 1):
            find_echos(text[i:])
        return len(echos)


'\n\naaaaaaaaaa\n2 + 4 + 6 + \n\n\nfor suffix pairs\ns[i:] s[j:] longest common prefix\n\n\nstore suffixes in a trie\n\n..abcdabceef\n\n\nabc..abc..\n\n'
