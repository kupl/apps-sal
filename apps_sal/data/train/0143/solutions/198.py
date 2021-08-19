class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # dynamic sliding windo
        maxi = 0
        if len(tree) == 1:
            return 1
        l = []
        s = set()
        for i in range(len(tree)):
            l.append(tree[i])
            s.add(tree[i])
            if len(s) > 2:  # we need to change the start of the window, remove until the size of set reduces to less than=2
                # l=l[::-1]
                while len(set(l)) > 2:
                    # l.pop()
                    l = l[1:]  # pop the first element until the set has less than equal to 2 elements
                # l=l[::-1]
                s = set(l)  # new version of set
            maxi = max(maxi, len(l))
        return maxi
# increasing the sizee of sliding window by starting at each element
#         maxi=0
#         if len(tree)==1:
#             return 1

#         for i in range(len(tree)):
#             s=set()
#             s.add(tree[i])
#             for j in range(i+1,len(tree)):
#                 s.add(tree[j])
#                 if len(s)>2:
#                     break
#                 maxi=max(maxi,j-i+1)
#         return maxi

        # for i in range(len(tree),0,-1):
        #     start=0
        #     end=i
        #     for j in range(len(tree)-i+1):
        #         s=tree[start:end]
        #         start+=1
        #         end+=1
        #         if len(set(s))<=2:
        #             return i
