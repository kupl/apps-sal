class Item:
    def __init__(self,label,value):
        self.label=label
        self.value=value

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        labelvalues=[]
        i=0
        while i <len(values):
            labelvalues.append(Item(labels[i],values[i]))
            i+=1
        lv=[]
        
        for item in labelvalues:
            heapq.heappush(lv,(-item.value,item.label))
        countlabels=collections.defaultdict(int)
        maximum_sum=0
        while num_wanted>0 and lv:
            max_value=heapq.heappop(lv)
            curr_max=max_value[0]
            curr_label_value=max_value[1]
            if countlabels.get(curr_label_value,0)<use_limit:
                countlabels[curr_label_value]+=1
                maximum_sum-=curr_max
                num_wanted-=1
        return maximum_sum
