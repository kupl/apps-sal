class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_arr = [ord(x) for x in s1]
        s2_arr = [ord(x) for x in s2]
        s1_arr.sort()
        s2_arr.sort()
        s1_counter = 0
        s2_counter = 0
        for i in range(len(s1_arr)):
            if s1_arr[i] > s2_arr[i]:
                s1_counter += 1
            elif s1_arr[i] == s2_arr[i]:
                s1_counter += 1
                s2_counter += 1
            else:
                s2_counter += 1
        print((s1_counter, s2_counter))
        if s1_counter == len(s1) or s2_counter == len(s1):
            return True
        else:
            return False
