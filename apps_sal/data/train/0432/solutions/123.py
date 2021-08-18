from typing import List
from collections import Counter
from sortedcontainers import SortedSet


class Solution:
    def isPossibleDivide(self, hand: List[int], W: int) -> bool:

        if not hand:
            return True
        elif len(hand) % W != 0:
            return False
        else:
            counts = Counter(hand)
            ns = SortedSet(list(counts.keys()))

            numRounds = len(hand) // W
            for r in range(numRounds):
                if len(ns) < W:
                    return False
                else:
                    nn = list(ns.islice(stop=W))
                    prev = ns[0] - 1
                    for n in nn:
                        if n == prev + 1:
                            counts[n] -= 1
                            if counts[n] == 0:
                                ns.remove(n)
                            prev = n
                        else:
                            return False

            return True
