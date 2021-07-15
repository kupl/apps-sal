class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # count = 0
        # from string import ascii_lowercase
        # for letter in ascii_lowercase:
        #     count += abs(t.count(letter) - s.count(letter))
        # return int(count//2)
        abc = 'abcdefghijklmnopqrstuvwxyz'
        return int(sum(abs(t.count(l)-s.count(l)) for l in abc)/2)
                

