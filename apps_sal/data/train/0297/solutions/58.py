class Solution:
    result = 0

    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        self.dfs(counter, [])
        return self.result

    def dfs(self, counter, curr):
        if curr:
            self.result += 1
        for x in counter:
            curr1 = curr.copy()
            counter1 = counter.copy()
            curr1.append(x)
            counter1[x] -= 1
            if counter1[x] == 0:
                del counter1[x]
            self.dfs(counter1, curr1)
