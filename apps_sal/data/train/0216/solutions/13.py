class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs, d = [], {c: [] for c in 'croak'}
        for c in croakOfFrogs:
            bucket = 'croak'['croak'.find(c)-1]
            if not d[bucket]:
                if bucket != 'k': return -1
                frogs.append([])
                d[c].append(len(frogs) - 1)
            else:
                d[c].append(d[bucket].pop())
                if c == 'c':
                    frogs[d[c][-1]].clear()
            frogs[d[c][-1]].append(c)
        return len(frogs) if all(len(frog) == 5 for frog in frogs) else -1

