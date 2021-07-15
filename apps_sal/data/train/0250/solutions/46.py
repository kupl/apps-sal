class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers = sorted([float(w) / q, q] for w, q in zip(wage, quality))
        #print('workers: ',workers)
        res = float('inf')
        qsum = 0
        heap = []
        
        def rec(l,r,heap,newQ):
            if l>r:
                heap.insert(l,newQ)
                return heap
            m=l+int((r-l)/2)
            if heap[m]>newQ:
                return rec(l,m-1,heap,newQ)
            else:
                return rec(m+1,r,heap,newQ)
            
        for r, q in workers:
            #print('before heap: ', heap)
            heap=rec(0,len(heap)-1,heap,q)
            #print('after heap: ', heap)
            qsum += q
            if len(heap) > K:
                
                p=heap.pop(K)
                #print('heapq.heappop(heap): ',p, 'r:', r, 'qsum: ',qsum)
                qsum += -p
            if len(heap) == K:
                res = min(res, qsum * r)
        return res
