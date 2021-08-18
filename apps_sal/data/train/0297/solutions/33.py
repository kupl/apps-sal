class Solution:

    def subsets(self, tiles, buff, buff_index, boolean, s):
        if tuple(buff[:buff_index]) not in s:
            s.add(tuple(buff[:buff_index]))
            self.count += 1
        if len(buff) == buff_index:
            return

        for i in range(0, len(tiles)):
            if not boolean[i]:
                buff[buff_index] = tiles[i]
                boolean[i] = True
                self.subsets(tiles, buff, buff_index + 1, boolean, s)
                boolean[i] = False

    def numTilePossibilities(self, tiles: str) -> int:
        self.count = 0
        buff = [None] * len(tiles)
        boolean = [False] * len(tiles)
        s = set()
        self.subsets(tiles, buff, 0, boolean, s)
        return self.count - 1
