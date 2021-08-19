class Solution:

    def distinctEchoSubstrings(self, text):
        base = 29
        mod = 10 ** 9 + 7
        aset = set()
        n = len(text)
        thash = [0] * (n + 1)
        tpow = [0] * (n + 1)
        tpow[0] = 1

        def getHash(l, r):
            return (thash[r] - thash[l] * tpow[r - l] % mod + mod) % mod
        for i in range(1, n + 1):
            thash[i] = (thash[i - 1] * base + ord(text[i - 1])) % mod
            tpow[i] = tpow[i - 1] * base % mod
        for alen in range(1, n // 2 + 1):
            l = 0
            r = alen
            counter = 0
            while l < n - alen:
                if text[l] == text[r]:
                    counter += 1
                else:
                    counter = 0
                if counter == alen:
                    aset.add(getHash(l - alen + 1, l + 1))
                    counter -= 1
                l += 1
                r += 1
        return len(aset)
        'public int distinctEchoSubstrings(String text) {\n\t\tSet<Long> set = new HashSet<>();\n\t\tint n = text.length();\n\t\tpreprocess(n, text);\n\n\t\tfor (int len = 1; len <= n / 2; len++) {\n\t\t\tfor (int l = 0, r = len, counter = 0; l < n - len; l++, r++) {\n\t\t\t\tif (text.charAt(l) == text.charAt(r)) {\n\t\t\t\t\tcounter++;\n\t\t\t\t} else {\n\t\t\t\t\tcounter = 0;\n\t\t\t\t}\n                \n                // 这个操作可以加速？！并不是所有的都是直接call getHash的！\n\t\t\t\tif (counter == len) {\n\t\t\t\t\tset.add(getHash(l - len + 1, l + 1));\n\t\t\t\t\tcounter--;\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\n\t\treturn set.size();\n\t}'

    def distinctEchoSubstrings1(self, text: str) -> int:
        base = 29
        mod = 10 ** 9 + 7
        aset = set()
        n = len(text)
        thash = [0] * (n + 1)
        tpow = [0] * (n + 1)
        tpow[0] = 1

        def getHash(l, r):
            return (thash[r] - thash[l] * tpow[r - l] % mod + mod) % mod
        for i in range(1, n + 1):
            thash[i] = (thash[i - 1] * base + ord(text[i - 1])) % mod
            tpow[i] = tpow[i - 1] * base % mod
        for i in range(n):
            for alen in range(2, n - i + 1, 2):
                mid = i + alen // 2
                hash1 = getHash(i, mid)
                hash2 = getHash(mid, i + alen)
                if hash1 == hash2:
                    aset.add(hash1)
        return len(aset)
        '\n        class Solution {\n        long BASE = 29L, MOD = 1000000007L;\n        public int distinctEchoSubstrings(String str) {\n            HashSet<Long> set = new HashSet<>();\n            int n = str.length();\n            long[] hash = new long[n + 1]; // hash[i] is hash value from str[0..i]\n            long[] pow = new long[n + 1]; // pow[i] = BASE^i\n            pow[0] = 1;\n            for (int i = 1; i <= n; i++) {\n                hash[i] = (hash[i - 1] * BASE + str.charAt(i - 1)) % MOD;\n                pow[i] = pow[i - 1] * BASE % MOD;\n            }\n            for (int i = 0; i < n; i++) {\n                for (int len = 2; i + len <= n; len += 2) {\n                    int mid = i + len / 2;\n                    long hash1 = getHash(i, mid, hash, pow);\n                    long hash2 = getHash(mid, i + len, hash, pow);\n                    if (hash1 == hash2) set.add(hash1);\n                }\n            }\n            return set.size();\n        }\n\n        long getHash(int l, int r, long[] hash, long[] pow) {\n            return (hash[r] - hash[l] * pow[r - l] % MOD + MOD) % MOD;\n        }\n    }\n    '
