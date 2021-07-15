class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        grp = []
        x, y = tree[0], 1
        for e in tree[1:]:
            if e==x:
                y+=1
            else:
                grp.append((x,y))
                x, y = e, 1
        grp.append((x,y))
        
        ret = 0
        pair, pair_sum = [], 0
        for i in range(len(grp)):
            x, y = grp[i]
            if x in pair:
                pair_sum += y
            else:
                if len(pair)<2:
                    pair = pair + [x]
                    pair_sum += y
                else:
                    pair = [grp[i-1][0]] + [x]
                    pair_sum = grp[i-1][1] + y
            # print(pair)
            # print(pair_sum)
            # print('***')
            ret = max(ret, pair_sum)
        return ret
            
            

