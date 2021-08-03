class Solution:
    def countVowelPermutation(self, n: int) -> int:
        pos = [1, 1, 1, 1, 1]
        newpos = [1, 1, 1, 1, 1]
        for i in range(1, n):
            newpos[0] = pos[1] + pos[2] + pos[4]
            newpos[1] = pos[0] + pos[2]
            newpos[2] = pos[1] + pos[3]
            newpos[3] = pos[2]
            newpos[4] = pos[2] + pos[3]

            pos[0] = newpos[0]
            pos[1] = newpos[1]
            pos[2] = newpos[2]
            pos[3] = newpos[3]
            pos[4] = newpos[4]
        return ((newpos[0] + newpos[1] + newpos[2] + newpos[3] + newpos[4]) % (10**9 + 7))
