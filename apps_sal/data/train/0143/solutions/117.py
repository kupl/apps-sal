class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        fruit_dict = collections.defaultdict(int)
        j,result,count=0,0,0
        for i,t in enumerate(tree):
            fruit_dict[t]+=1
            count+=1
            while len(fruit_dict)>2 and j<len(tree):
                fruit_dict[tree[j]]-=1
                count-=1
                if fruit_dict[tree[j]]==0:
                    del fruit_dict[tree[j]]
                j+=1
            if len(fruit_dict)<=2:
                result = max(result,count)
        return result
        '''
        blocks = [(k,len(list(v))) for k,v in itertools.groupby(tree)]
        i,result=0,0
        
        while i<len(blocks):
            j=i
            count=0
            fruit_set = set()
            while j<len(blocks):
                fruit_set.add(blocks[j][0])
                count+=blocks[j][1]
                if len(fruit_set)>2:
                    i=j-1
                    break
                result=max(result,count)
                j+=1
            else:
                break
            
        return result
        '''
