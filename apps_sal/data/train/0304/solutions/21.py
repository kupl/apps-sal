class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages = sorted(ages)
        count, temp_count = 0, 0
        for i in range(len(ages) - 1, -1, -1):
            if i + 1 < len(ages) and ages[i + 1] == ages[i]:
                count += temp_count
                continue

            temp_count, current = 0, i - 1
            age = 0.5 * ages[i] + 7
            while current >= 0 and ages[current] > age:
                temp_count += 1
                current = current - 1

            count = count + temp_count

        return count
