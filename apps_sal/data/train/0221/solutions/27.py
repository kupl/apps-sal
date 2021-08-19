class Solution:
    def findRepSubstrGivenLength(self, nums: List[int], l: int, base: int, modulus: int) -> int:

        n = len(nums)

        h = 0
        for i in range(l):
            h = (h * base + nums[i]) % modulus

        seen = {h}

        for start in range(1, n - l + 1):
            h = (h * base - nums[start - 1] * pow(base, l, modulus) + nums[start + l - 1]) % modulus

            if h in seen:
                return start

            seen.add(h)

        return -1

    def longestDupSubstring(self, S: str) -> str:
        if not S:
            return ''

        nums = [ord(S[i]) - ord('a') for i in range(len(S))]

        base = 26
        modulus = 2**32

        left = 1
        right = len(S)

        while left <= right:
            mid = left + (right - left) // 2

            if self.findRepSubstrGivenLength(nums, mid, base, modulus) != -1:
                left = mid + 1
            else:
                right = mid - 1

        start = self.findRepSubstrGivenLength(nums, left - 1, base, modulus)

        return S[start: start + left - 1]


'''
class Solution:
    class Node:
        def __init__(self, v='*'): 
            self.value = v
            self.next = dict()
            self.occurences = set()
                   
                
    def print_tree(self, node, indentation):
        print(indentation + str(node.value) + \": \" + str(node.occurences))

        for v in node.next.keys():
            self.print_tree(node.next[v], indentation + '\\t')
        
        
    def getNode(self, node, v):
        if v not in node.next.keys():
            node.next[v] = self.Node(v)

        return node.next[v]


    def AddOccurences(self, node, i, S):
        node.occurences.add(i)

        if len(node.occurences) == 2:
            for o in node.occurences:
                if o + 1 < len(S):
                    self.AddOccurences(self.getNode(node, S[o+1]), o+1, S)


        if len(node.occurences)>2:
            if i + 1 < len(S):
                self.AddOccurences(self.getNode(node, S[i+1]), i+1, S)

        
    def getLongestDuplicate(self, node):
        maxSubstring = ''
        
        for v in node.next.keys():
            if len(node.next[v].occurences)>1:

                childSubstring = self.getLongestDuplicate(node.next[v])
                if len(childSubstring) + 1 > len(maxSubstring):
                    maxSubstring = v + childSubstring
                        
        return maxSubstring
    
    
    def longestDupSubstring(self, S: str) -> str:
        if not S:
            return 0
        
        if len(set(S)) == 1:
            return S[0:len(S)-1]

        root = self.Node()

        for i in range(len(S)):
            self.AddOccurences(self.getNode(root, S[i]), i, S)

        #self.print_tree(root, '')
        maxDepthDuplicates = self.getLongestDuplicate(root)
        
        return maxDepthDuplicates
'''
