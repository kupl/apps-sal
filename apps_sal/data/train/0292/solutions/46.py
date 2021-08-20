class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        case_1_max = case_2_max = case_3_max = case_4_max = -float('inf')
        case_1_min = case_2_min = case_3_min = case_4_min = float('inf')
        for i in range(len(arr1)):
            case_1_max = max(case_1_max, arr1[i] + arr2[i] - i)
            case_1_min = min(case_1_min, arr1[i] + arr2[i] - i)
            case_2_max = max(case_2_max, arr1[i] - arr2[i] - i)
            case_2_min = min(case_2_min, arr1[i] - arr2[i] - i)
            case_3_max = max(case_3_max, arr2[i] - arr1[i] - i)
            case_3_min = min(case_3_min, arr2[i] - arr1[i] - i)
            case_4_max = max(case_4_max, arr2[i] + arr1[i] + i)
            case_4_min = min(case_4_min, arr2[i] + arr1[i] + i)
        return max(case_1_max - case_1_min, case_2_max - case_2_min, case_3_max - case_3_min, case_4_max - case_4_min)
