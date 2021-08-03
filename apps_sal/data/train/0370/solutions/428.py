from typing import *

import math
import collections


class UnionFindGraph(dict):
    def union(self, p: Hashable, q: Hashable):
        rootOfP = self.root(p)
        rootOfQ = self.root(q)
        self[rootOfP] = rootOfQ

    def root(self, p: Hashable) -> Hashable:

        while p != self[p]:
            self[p] = self[self[p]]
            p = self[p]

        return p

    def isConnected(self, p: Hashable, q: Hashable) -> bool:
        return self.root(p) == self.root(q)


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        mapping = UnionFindGraph()
        divisorNumberMapping = dict()

        for v in A:
            if v == 1:
                continue

            if v not in divisorNumberMapping:
                divisorNumberMapping[v] = set()
            divisorNumberMapping[v].add(v)

            if v not in mapping:
                mapping[v] = v

            for w in divisorNumberMapping[v]:
                if w != v:
                    mapping.union(v, w)
                    break

            for i in range(2, math.ceil(math.sqrt(v)) + 1):
                if v % i == 0 and (v // i) != 1:
                    if i not in divisorNumberMapping:
                        divisorNumberMapping[i] = set()
                    if (v // i) not in divisorNumberMapping:
                        divisorNumberMapping[v // i] = set()

                    divisorNumberMapping[i].add(v)
                    divisorNumberMapping[v // i].add(v)

                    for w in divisorNumberMapping[i]:
                        if v != w:
                            mapping.union(v, w)
                            break

                    for w in divisorNumberMapping[v // i]:
                        if v != w:
                            mapping.union(v, w)
                            break

        counter = collections.Counter(
            mapping.root(k) for k in mapping)
        # print(mapping)
        return max(counter.values())
