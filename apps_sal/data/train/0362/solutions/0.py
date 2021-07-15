class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # assign hat to people
        n = len(hats)
        dic = collections.defaultdict(list)
        for i,hat in enumerate(hats):
            for h in hat:
                dic[h].append(i)
        
        # mask for people: ways
        bfs = {0:1}
        target = (1<<n)-1
        res = 0
        for h in range(1,41):
            new_bfs = bfs.copy()
            for p in dic[h]:
                for mask,cnt in list(bfs.items()):
                    new_mask = (1<<p)|mask
                    if new_mask!=mask:
                        if new_mask not in new_bfs:
                            new_bfs[new_mask]=0
                        new_bfs[new_mask]+= cnt
            bfs = new_bfs
        return bfs[target]%(10**9+7) if target in bfs else 0

