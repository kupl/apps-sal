class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        # convert s to t in k moves or less
        # so the ith move is 1 <= i <= k
        # pick a character at j (1-indexed) in the string and shift it i times
        # or you can do nothing in the move.
        # 'shifting' the character means to replace it to the next letter in the alphabet
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        # any index j can be picked at most ONCE
        # for each x  [1..k] you have an opportunity to shift a character in s, i times.
        # the answer is false if there is a character that needs more shifts than we are able to supply
        # can create a list of deltas, sorted descending, and see if we have enough space to work with
        deltas = []
        if len(s) != len(t): return False
        for i,c in enumerate(s):
            t_index = ord(t[i]) - ord('a')
            s_index = ord(s[i]) - ord('a')
            deltas.append((t_index - s_index)%26)
        m = collections.defaultdict(int)
        while k%26 != 0:
            m[k%26] += 1
            k -= 1
        for i in range(1,26):
            m[i] += k//26
        #print(sorted(deltas, reverse=True))
        for d in sorted(deltas, reverse=True):
            if not d:
                continue
            if not m[d]:
                return False
            m[d] -= 1
            # take the highest available k that will satisfy that delta
            # ie, take the highest number x such that x%26 == d %26
            # or you can have a count of all the numbers that land in each class
        return True
