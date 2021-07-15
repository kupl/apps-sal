'''
{3:1,1:1}

'''
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        first,sec=0,0
        curr_hash={}
        if len(tree)<3:return len(tree)
        Max=[float('-inf')]
        while(first<len(tree)):
            first=self.first_pass(first,curr_hash,tree,Max)
            if first>len(tree):continue
            sec=self.sec_pass(sec,first,curr_hash,tree)
        return Max[0]
    def first_pass(self,pointer,hash,trees,Max):
        count=0
        for key in hash:
            count+=hash[key]
        while(pointer<len(trees)):
            typ=trees[pointer]
            if typ in hash:hash[typ]+=1
            else:
                if len(hash)<2:
                    hash[typ]=1
                else:
                    break
            count+=1
            pointer+=1
        Max[0]=max(Max[0],count)
        return pointer
    
    def sec_pass(self,sec,first,hash,tree):
        while(sec<first and len(hash)>1):
            typ=tree[sec]
            if hash[typ]==1: del hash[typ]
            else: hash[typ]-=1
            sec+=1
        return sec
        

