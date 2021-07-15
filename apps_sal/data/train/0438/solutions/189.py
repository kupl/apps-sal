class Solution:
    
    def find_root(self, arr, idx):
        assert arr[idx][0] != -1
        while(arr[idx][0] != idx):
            idx = arr[idx][0]
        return idx
        
    def findLatestStep(self, arr: List[int], m: int) -> int:
        tree_root = [[-1,-1] for i in range(len(arr))]
        
        if m == len(arr):
            return m
        
        last_t = -1
        for i in range(len(arr)):
            bit_idx = arr[i] - 1
            for j in range(bit_idx-1, bit_idx+2):
                if 0 <= j < len(arr):
                    if tree_root[j][0] != -1 and tree_root[self.find_root(tree_root, j)][1] == m:
                        last_t = i
                        
            tree_root[bit_idx][0] = bit_idx
            tree_root[bit_idx][1] = 1
            if bit_idx > 0 and tree_root[bit_idx-1][0] != -1:
                left_node_root = self.find_root(tree_root, bit_idx-1)
                tree_root[left_node_root][0] = bit_idx
                tree_root[bit_idx][1] += tree_root[left_node_root][1]
            if bit_idx < len(arr)-1 and tree_root[bit_idx+1][0] != -1:
                right_node_root = self.find_root(tree_root, bit_idx+1)
                tree_root[right_node_root][0] = bit_idx
                tree_root[bit_idx][1] += tree_root[right_node_root][1]
            
            # for j in range(len(arr)):
            #     if (tree_root[j][0] == j and tree_root[j][1] == m):
            #         last_t = i + 1
            
            # if (tree_root[bit_idx][1] == m):
            #     last_t = i + 1
        
        return last_t
