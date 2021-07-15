class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A = sorted(A)
        n = len(A)
        dict_num = {}
        for num in A:
            dict_num[num] = True
        dp_dict = {}
        factor_pair = []
        for i in range(n):
            factor_pair.append([])
        
        for i in range(n):
            for j in range(i):
                if(A[i] % A[j] == 0 and A[i]//A[j] in dict_num):
                    factor_pair[i].append((A[j], A[i]//A[j]))
        # print(factor_pair)
        for i in range(n):
            root = A[i]
            num_trees = 1
            for a, b in factor_pair[i]:
                num_trees += dp_dict[a]*dp_dict[b]
            
            dp_dict[root] = num_trees
        
        answer = 0
        for key in dp_dict:
            answer += dp_dict[key]
            
        return answer % (10**9+7)
