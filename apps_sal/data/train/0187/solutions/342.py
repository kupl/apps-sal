class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        # we have the boardingCost and the runningCost
        # at each index we need to wipe it out before we move to the next
        # we can board max 4 at a time
        arr = [-1]

#         for i in range(len(customers)):
#             if customers[i] == 0:
#                 print('6')
#             else:
#                 divided = customers[i]//4;
#                 if customers[i] % 4 != 0:
#                     divided += 1;

#                 bammer = customers[i] * boardingCost - (divided * runningCost);
#                 arr.append(bammer);

#         print(max(arr));

        currentCost = 0
        maximum = -1000000000
        rotations = 0
        total = 0

        while (total != 0 or rotations < len(customers)):
            if (rotations < len(customers)):
                total += customers[rotations]
            if total < 4:
                temp = total
                total = 0
                currentCost += (temp * boardingCost) - runningCost
                arr.append(currentCost)
                if (currentCost > maximum):
                    maximum = currentCost
            else:
                total -= 4
                currentCost += (4 * boardingCost) - runningCost
                arr.append(currentCost)

            rotations += 1

        maxer = -1000000000
        indexer = -1

        for i in range(len(arr)):
            if (maxer < arr[i]):
                maxer = arr[i]
                indexer = i

        if indexer == 0:
            return -1
        return indexer
        # print(arr);
        # return max(arr);
