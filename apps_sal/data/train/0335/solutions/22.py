class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        deltaBase = {0:0}
        deltaList = [0]
        rods.sort()
        for rod in rods:
            # print(deltaList)
            # print(deltaBase)
            deltaBaseTemp = deltaBase.copy()
            iMax = len(deltaList)
            for i in range(iMax):
                delta = deltaList[i]
                deltaPlus = delta+rod   
                # print(rod, delta, deltaPlus)
                if deltaPlus not in deltaBase:
                    deltaList.append(deltaPlus)
                    deltaBase[deltaPlus] = deltaBaseTemp[delta]
                else:
                    deltaBase[deltaPlus] = max(deltaBase[deltaPlus], deltaBaseTemp[delta])

                
                deltaMinus = delta-rod
                if deltaMinus > 0:
                    if deltaMinus not in deltaBase:
                        deltaList.append(deltaMinus)
                        deltaBase[deltaMinus] = deltaBaseTemp[delta]+ rod
                    else:
                        deltaBase[deltaMinus] = max(deltaBase[deltaMinus], deltaBaseTemp[delta]+ rod)
                else:
                    deltaMinus = -deltaMinus
                    if deltaMinus not in deltaBase:
                        deltaList.append(deltaMinus)
                        deltaBase[deltaMinus] = deltaBaseTemp[delta]+ rod - deltaMinus
                    else:
                        deltaBase[deltaMinus] = max(deltaBase[deltaMinus], deltaBaseTemp[delta]+ rod - deltaMinus)
        #         print(rod, delta, deltaMinus, deltaBaseTemp[delta]+ rod - deltaMinus)
        # print(deltaList)
        # print(deltaBase)
        return deltaBase[0]
