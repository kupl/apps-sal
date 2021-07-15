class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        profitDict = defaultdict(dict)
        profitList = [(g, p) for g, p in zip(group, profit)]
        profitList.sort()
        ans = 0
        for g,p in profitList:
            # newProfit = set()
            newProfitDict = defaultdict(dict)
            for p0 in list(profitDict.keys()):
                thisProfit = p0 + p
                for preG in list(profitDict[p0].keys()):
                    thisG = preG + g
                    if thisG > G:
                        profitDict[p0].pop(preG)
                    else:
                        if thisProfit >= P:
                            ans += profitDict[p0][preG]
                        if thisG in newProfitDict[thisProfit]:               
                            newProfitDict[thisProfit][thisG] += profitDict[p0][preG]
                        else:
                            newProfitDict[thisProfit][thisG] = profitDict[p0][preG]
                
            for profitTemp in newProfitDict:
                for groupTemp in newProfitDict[profitTemp]:
                    if groupTemp in profitDict[profitTemp]:   
                        profitDict[profitTemp][groupTemp] += newProfitDict[profitTemp][groupTemp]
                    else:
                        profitDict[profitTemp][groupTemp] = newProfitDict[profitTemp][groupTemp]
    
            if g <= G and p >=P:
                ans += 1
            if g in profitDict[p]:
                profitDict[p][g] += 1
            else:
                profitDict[p][g] = 1
        return ans%(10**9+7)
