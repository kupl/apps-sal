
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []


        candidates = sorted(candidates)
        print(candidates)

        results = []


        def find(curr_comb, curr_sum, candidates): #靠副作用填充results
            #curr_comb = curr_comb[:]
            for i,cand in enumerate(candidates):

                if (cand+curr_sum) < target:
                    new_curr_comb = curr_comb[:]
                    new_curr_comb.append(cand)
                    find(new_curr_comb, curr_sum+cand, candidates[i+1:])
                elif (cand+curr_sum) == target:
                    new_curr_comb = curr_comb[:]
                    new_curr_comb.append(cand)
                    if new_curr_comb not in results:
                        results.append(new_curr_comb)
                    #print(curr_comb, curr_sum, cand, 'target:',target)
                else:
                    break


        find([], 0, candidates)

        return results