class Solution:
    def counts(self, collect):
        answer = 1
        for char in collect:
            if collect[char]:
                answer += self.counts(collect - collections.Counter(char))
        return answer

    def numTilePossibilities(self, c):
        return self.counts(collections.Counter(c)) - 1
