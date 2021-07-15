class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # get length of array 
        length = len(arr)
        # build dict to count how many times each int appears
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] =1
            else:
                counts[num] += 1
                
        # print(counts)
        
        # get values from dict, sort in descending order
        descending = sorted(counts.values(), reverse =  True)
        # print(descending)
        # initialize 2 variables: count and total
        count = 0
        total = 0
        # loop over descending list of counts
        for num in descending:
            # add each number to our total
            total += num
            # increment count by 1
            count += 1
            # if our total is half or more, return count
            if total >= length/2:
                return count
