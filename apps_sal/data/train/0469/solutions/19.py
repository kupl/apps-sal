class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dic = collections.defaultdict(list)
        for idx, (left , right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                dic[left].append(idx)
            if right != -1:
                dic[right].append(idx)
      
        parent = set()
        for key, value in dic.items():
            if len(value) > 1:
                return False
            if [key]  == dic.get(value[0], []):
                return False
            parent.add(value[0])
            
        if parent and len(dic.keys() - parent) == 0:
            return False
        
        return len(dic) == n-1        
