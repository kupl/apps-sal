class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        s = seats
        first = 0
        second = 0
        second_index = 0
        output = []
        Set = False
        count = 0
        for i in range(len(s)):
            if s[i] != 1:
                if Set == False:
                    count = count + 1
                continue
            else:
                Set = True
                for j in range(i + 1, len(s)):
                    if s[j] != 1:
                        second_index = j
                        continue
                    else:
                        second_index = j
                        print((second_index, i))
                        break
                diff = second_index - i
                if second_index == len(s) - 1 and s[second_index] == 0:
                    output.append(diff)
                output.append(count)
                if diff % 2 == 0:
                    output.append(int(diff / 2))
                else:
                    output.append(int(diff / 2))
        return max(output)
