class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        days = [1 if hour > 8 else -1 for hour in hours] #find longest strictly positive subarr
        prefSums = days[:]
        for i in range(1, len(hours)):
            prefSums[i] = days[i] + prefSums[i - 1]
        result = 0
        prefixLookup = {}
        for i in range(len(hours)):
            sumToHere = prefSums[i] #longest answer ending here 
            if sumToHere >= 1:
                result = max(result, i + 1)
            else:
                earlierPrefSumNeeded = sumToHere - 1
                if earlierPrefSumNeeded in prefixLookup:
                    result = max(result, i - prefixLookup[earlierPrefSumNeeded])
            if sumToHere not in prefixLookup:
                prefixLookup[sumToHere] = i
        return result

