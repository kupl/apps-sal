class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, numLettersToRemove):
        dictionary = {}

        for num in arr:
            if num in dictionary:
                dictionary[num] = dictionary[num] + 1
            else:
                dictionary[num] = 1

        dictionary = {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[1])}

        keyList = list(dictionary.keys())
        valueList = list(dictionary.values())
        keyPointer = 0
        valuePointer = 0
        while numLettersToRemove > 0:

            if (valueList[valuePointer] > 0):
                valueList[valuePointer] = valueList[valuePointer] - 1

            if valueList[valuePointer] == 0:
                keyPointer += 1
                valuePointer += 1

            numLettersToRemove -= 1

        outputList = keyList[keyPointer:]

        output = outputList.__len__()

        return output
