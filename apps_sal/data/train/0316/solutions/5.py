class Solution:
    def longestPrefix(self, s: str) -> str:
        '''
        res keeps track of the index of the end of the prefix, used to output the happy prefix
        l stores the hash key for prefix
        r tracks the hash key for suffix
        '''
        res, l, r = 0, 0, 0
        mod = 10**9 + 5  # used to ensure that the hash value doesn't overflow
        '''
        now start from the beginning and end of the string
        - note you shouldn't search teh whole string because the longest prefix/suffix is the string itself
        '''
        for i in range(len(s) - 1):
            # hash the prefix/suffix in o(1); 128 can be substituted with any value; it just happens to be the length of ASCII
            '''
            for a given string 'elkmmmelk', prefix elk will be hashed in ascending order.
            e: 'e': hash[e] = ord(e)
            l: 'el': hash[el] = hash(e)*128 + ord(l)
            k: 'elk': hash[elk] = hash(el)*128 + ord(k)
            which translates to (l * 128 + ord(s[i]))

            suffix elk will be hashed in descending order
            k: 'k': hash[k] = ord(k)
            l: 'lk': hash[lk] = ord(k) + ord(l) * 128
            e: 'elk': hash[elk] = ord(k) + ord(l) * 128 + ord(e) * 128^2
            which translates to r + pow(128, i, mod)
            '''
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[-i - 1])) % mod
            if l == r:  # if both hash values match, update res
                res = i + 1
        return s[:res]
