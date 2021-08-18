class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def findZerosBefore(index, array):
            zerosBefore = 0
            index -= 1
            while (index >= 0 and array[index] != 1):
                zerosBefore += 1
                index -= 1
            return zerosBefore

        def findZerosAfter(index, array):
            zerosAfter = 0
            index += 1
            while (index < len(array) and array[index] != 1):
                zerosAfter += 1
                index += 1
            return zerosAfter

        def zeroString(index, array):
            zeros = 0
            while (index < len(array) and array[index] != 1):
                zeros += 1
                index += 1

            return zeros

        def zeroCombs(n):
            combs = 0
            for i in range(n, 0, -1):
                combs = combs + n - i + 1
            return combs

        def firstZero(index, array):
            if (index == 0):
                return True
            if (array[index - 1] == 1):
                return True
            else:
                return False

        total = 0

        if (S > 0):
            one_array = [i for i, one in enumerate(A) if one == 1]
            print(one_array)
            start_index = []
            end_index = []

            for n in range(len(one_array)):
                if (n + S - 1 < len(one_array)):
                    start_index.append(one_array[n])
                    end_index.append(one_array[n + (S - 1)])
            print(start_index)
            print(end_index)
            for i in range(len(start_index)):
                Bef = findZerosBefore(start_index[i], A)
                print(Bef)
                Aft = findZerosAfter(end_index[i], A)
                total = total + Bef + Aft + (Bef * Aft) + 1

        if (S == 0):
            zero_array = [i for i, zero in enumerate(A) if zero == 0]
            for n in range(len(zero_array)):
                if (firstZero(zero_array[n], A)):
                    sticky = zeroString(zero_array[n], A)
                    total = int(total + (sticky**2 + sticky) / 2)

        return total
