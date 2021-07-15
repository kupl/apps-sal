class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = imax = 0
        for i, a in enumerate(A):
            res = max(res, imax + A[i] - i)
            imax = max(imax, A[i] + i)
        return res

#     int n = a.size();
#     int maxOverallGain = INT_MIN;
#     int maxEndRight = a[n-1] - (n-1);
#     for(int i=n-2; i>=0; i--)
#     {
#         maxEndRight = max(maxEndRight, a[i+1] - (i+1));
#         maxOverallGain = max(maxOverallGain, a[i] + i + maxEndRight);
#     }
#     return maxOverallGain;

