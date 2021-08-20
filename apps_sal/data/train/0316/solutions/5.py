class Solution:

    def longestPrefix(self, s: str) -> str:
        """
        res keeps track of the index of the end of the prefix, used to output the happy prefix
        l stores the hash key for prefix
        r tracks the hash key for suffix
        """
        (res, l, r) = (0, 0, 0)
        mod = 10 ** 9 + 5
        "\n        now start from the beginning and end of the string\n        - note you shouldn't search teh whole string because the longest prefix/suffix is the string itself\n        "
        for i in range(len(s) - 1):
            "\n            for a given string 'elkmmmelk', prefix elk will be hashed in ascending order.\n            e: 'e': hash[e] = ord(e)\n            l: 'el': hash[el] = hash(e)*128 + ord(l)\n            k: 'elk': hash[elk] = hash(el)*128 + ord(k)\n            which translates to (l * 128 + ord(s[i]))\n\n            suffix elk will be hashed in descending order\n            k: 'k': hash[k] = ord(k)\n            l: 'lk': hash[lk] = ord(k) + ord(l) * 128\n            e: 'elk': hash[elk] = ord(k) + ord(l) * 128 + ord(e) * 128^2\n            which translates to r + pow(128, i, mod)\n            "
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[-i - 1])) % mod
            if l == r:
                res = i + 1
        return s[:res]
