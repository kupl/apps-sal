class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        result = set()

        def backtrack(left_tiles, curr_seq):
            if len(curr_seq) == k:
                result.add(''.join(curr_seq))
                return
            else:
                for i in range(len(left_tiles)):
                    curr_seq.append(left_tiles[i])
                    backtrack(left_tiles[:i] + left_tiles[i + 1:], curr_seq)
                    curr_seq.pop()
        for k in range(1, len(tiles) + 1):
            backtrack(tiles, [])
        return len(result)
