from typing import List
from sortedcontainers import SortedDict


class Solution:

    def isPossibleDivide(self, hand: List[int], W: int) -> bool:
        if not hand:
            return True
        elif len(hand) % W != 0:
            return False
        else:
            numPos = SortedDict()
            for (idx, n) in enumerate(hand):
                if n in numPos:
                    numPos[n].append(idx)
                else:
                    numPos[n] = [idx]
            numRounds = len(hand) // W
            for r in range(numRounds):
                if len(numPos) < W:
                    return False
                else:
                    ll = list(numPos.islice(stop=W))
                    prev = ll[0] - 1
                    for n in ll:
                        if n == prev + 1:
                            numPos[n].pop()
                            if not numPos[n]:
                                del numPos[n]
                            prev = n
                        else:
                            return False
            return True
