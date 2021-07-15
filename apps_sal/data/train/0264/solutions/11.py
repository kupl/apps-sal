class Solution:
    def maxLength(self, arr: List[str]) -> int:
        #array with all possible unique string combinations so far

        possible_strings = ['']
        maximum = 0
        for i in range(len(arr)):
            temp_len = len(possible_strings)
            for j in range(temp_len):
                #trying combination
                x = arr[i] + possible_strings[j]
                #string is unique
                if (len(x)==len(set(x))):
                    #append to possible strings
                    possible_strings.append(x)
                    #set max
                    maximum = max(maximum,len(x))
        return maximum


