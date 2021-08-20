class Solution:

    def getMax(self, arr, k, idx, cache):
        if idx == len(arr) - 1:
            return arr[idx]
        maxSum = 0
        for numInPartition in range(1, k + 1):
            if idx + numInPartition > len(arr):
                break
            startOfRecursiveIndex = idx + numInPartition
            maxVal = max(arr[idx:startOfRecursiveIndex])
            partSum = maxVal * numInPartition
            rest = cache[startOfRecursiveIndex] if startOfRecursiveIndex in cache else self.getMax(arr, k, startOfRecursiveIndex, cache)
            cache[startOfRecursiveIndex] = rest
            maxSum = max(maxSum, partSum + rest)
        return maxSum

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        """
        Input:
            A: int[] - Array of numbers
            K: int - Max length allowable for subarray

        Output:
            Return largest sum after partitioning.

        Steps:
            1. Make partition
            2. Change all elements to max value

           v            
        [1,2,9,30], 2

        {1,2}{9,30} => {2,2}{30,30} => 4 + 60 = 64
        {1}{2,9}{30} => {1}{9,9}{30} => 1 + 18 + 30 = 49


        Example:
            [1]
            {1} = 1

            [1,2]
            {1}{2} => 1+2 = 3
            {1,2} => {2,2} => 4
                 v
            [1,2,9]
            {1,2}{9} => {2,2} + {9} => 4 + 9 = 13
            {1}{2,9} => {1},{9,9} = 1 + 18 = 19
            {1,2,9}

            {1}{2,9}{30} => {1}{9,9}{30} => 19 + 30 => 49
            {1,2}{9,30} => {2,2}{30,30} => 4 + 60 => 64

                 v
            [1,2,9,30]
            {1,2,9} {30} => 30 + getMaxSum([1,2,9]) => 30 + 19 => 49
            {1,2} {9,30} => 60 + getMaxSum([1,2]) => 60 + 4 = 64

            {1}{2,9,30}
            {1,2}{9,30}
            {1,2,9}{30}

        All about subproblems!!

        Approach:
            - Let's look into sliding window.
            - We can frame this problem in terms of choices.
                When considering an element, we can place it into its own partition OR with the preceeding partition.
                Choice:
                    K-way choice
                    Do I group my current element in the last [1,k] elements?
                Constraint:
                    Subset needs to be contiguous?
                Goal:
                    Maximum sum

            1. When placing
        Approach:
            [0,0,0,0]
            maxSum[i] = max(maxSum[i-1] + A[i] * 1, maxSum[i-2] + max(last two elements) * 2) and so on
        """
        cache = {}
        return self.getMax(A, K, 0, cache)
