class Solution:

    def distinctEchoSubstrings(self, text):
        base = 29
        mod = 10**9 + 7

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
        '''public int distinctEchoSubstrings(String text) {
\t\tSet<Long> set = new HashSet<>();
\t\tint n = text.length();
\t\tpreprocess(n, text);

\t\tfor (int len = 1; len <= n / 2; len++) {
\t\t\tfor (int l = 0, r = len, counter = 0; l < n - len; l++, r++) {
\t\t\t\tif (text.charAt(l) == text.charAt(r)) {
\t\t\t\t\tcounter++;
\t\t\t\t} else {
\t\t\t\t\tcounter = 0;
\t\t\t\t}
                
                // 这个操作可以加速？！并不是所有的都是直接call getHash的！
\t\t\t\tif (counter == len) {
\t\t\t\t\tset.add(getHash(l - len + 1, l + 1));
\t\t\t\t\tcounter--;
\t\t\t\t}
\t\t\t}
\t\t}

\t\treturn set.size();
\t}'''

    def distinctEchoSubstrings1(self, text: str) -> int:
        base = 29
        mod = 10**9 + 7

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

        '''
        class Solution {
        long BASE = 29L, MOD = 1000000007L;
        public int distinctEchoSubstrings(String str) {
            HashSet<Long> set = new HashSet<>();
            int n = str.length();
            long[] hash = new long[n + 1]; // hash[i] is hash value from str[0..i]
            long[] pow = new long[n + 1]; // pow[i] = BASE^i
            pow[0] = 1;
            for (int i = 1; i <= n; i++) {
                hash[i] = (hash[i - 1] * BASE + str.charAt(i - 1)) % MOD;
                pow[i] = pow[i - 1] * BASE % MOD;
            }
            for (int i = 0; i < n; i++) {
                for (int len = 2; i + len <= n; len += 2) {
                    int mid = i + len / 2;
                    long hash1 = getHash(i, mid, hash, pow);
                    long hash2 = getHash(mid, i + len, hash, pow);
                    if (hash1 == hash2) set.add(hash1);
                }
            }
            return set.size();
        }

        long getHash(int l, int r, long[] hash, long[] pow) {
            return (hash[r] - hash[l] * pow[r - l] % MOD + MOD) % MOD;
        }
    }
    '''
