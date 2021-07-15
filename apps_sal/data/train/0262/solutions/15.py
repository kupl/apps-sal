class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        def solve(i, j, carry):
            # The current column assignment is over, so check for validity
            if j == len(words): 
                csum = carry
                for k in range(len(words)):
                    csum += 0 if i >= len(words[k]) else assign[words[k][i]] 
                # We have come to column i, but the result itself is not long enough.    
                if i >= len(result): return False 
                if result[i] in assign:
                    return csum % 10 == assign[result[i]] and solve(i+1, 0, csum // 10) # i th char of result  is already assigned, so check if its valid and go to next column i+1 and start from word 0
                else:
                    # If the current digit can't be assigned to ith char of result or if its 0 and we are looking at first char of a word: then return False
                    if (csum % 10) in assign.values() or (csum % 10 == 0 and i == len(result) - 1):
                        return False
                    assign[result[i]] = csum % 10
                    ret = solve(i+1, 0, csum // 10)
                    del assign[result[i]]
                    return ret
                
            if i == len(result): 
                return i >= max(len(w) for w in words)  and carry == 0 and all(assign[w[len(w)-1]] != 0 for w in words + [result])
            # Handle length of word less than the column we are looking at OR the ith column char of the jth word is already assigned previously
            if i >= len(words[j]) or words[j][i] in assign: return solve(i, j+1, carry)     
            for val in range(10):
                if val == 0 and i == len(words[j]) - 1: continue  # Handle not to assign 0 for first letter of a word 
                if val not in assign.values():
                    assign[words[j][i]] = val
                    ret = solve(i, j+1, carry)
                    if ret: return True
                    del assign[words[j][i]]   
            return False
        
        result = result[::-1]
        words = [w[::-1] for w in words]
        assign = dict()
        return solve(0, 0, 0)
