class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        num_count_dict = {}
        for num in arr:
            if num in num_count_dict:
                num_count_dict[num] += 1
            else:
                num_count_dict[num] = 1

        num_dict = {}
        for num in num_count_dict.keys():
            count = num_count_dict[num]
            if count in num_dict:
                num_dict[count].append(num)
            else:
                num_dict[count] = [num]

        sorted_num_by_count = sorted(num_count_dict.items(), key=lambda x: x[1])
        print(sorted_num_by_count)
        for i in range(0, len(sorted_num_by_count)):
            num = sorted_num_by_count[i][0]
            num_count = num_count_dict[num]
            if num_count <= k:
                del num_count_dict[num]
            else:
                num_count_dict[num] = num_count_dict[num] - k
            k = k - num_count
            if k == 0:
                break
        return len(num_count_dict)
