class Solution:
    def soupServings(self, N):
        if N >= 5551:
            return 1
        self.dd = collections.defaultdict(float)
        return self.sub(N, N)

    def sub(self, an, bn):
        if an <= 0 and bn <= 0:
            return 0.5
        if an <= 0:
            return 1
        if bn <= 0:
            return 0
        if (an, bn) in self.dd:
            return self.dd[(an, bn)]
        c1 = self.sub(an - 100, bn)
        c2 = self.sub(an - 75, bn - 25)
        c3 = self.sub(an - 50, bn - 50)
        c4 = self.sub(an - 25, bn - 75)
        self.dd[(an, bn)] = 0.25 * sum([c1, c2, c3, c4])
        return self.dd[(an, bn)]
