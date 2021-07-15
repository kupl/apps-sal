class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        hashmap = collections.defaultdict(int)
        
        maxHeap = [(-v,labels[i]) for i,v in enumerate(values)]
        heapq.heapify(maxHeap)
        out = 0
        while num_wanted>0:
            if len(maxHeap)==0: 
                break 
            value, label = heapq.heappop(maxHeap)
            if hashmap[label]<use_limit:
                hashmap[label] = hashmap[label] +1 
                num_wanted -= 1
                out = out - value
        return out
        

