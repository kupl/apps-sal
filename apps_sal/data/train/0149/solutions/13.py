class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        len_s = len(s)

        if k > len_s:
            return s

        def helper(string, itr_range):
            not_found = False  # if no k repeating elements found, then True

            while not not_found:
                not_found = True

                for i in range(itr_range):
                    if string[i:i + k] == string[i] * k:
                        string = string[:i] + string[i + k:]
                        itr_range = len(string) - k + 1
                        not_found = False
                        break
            return string

        return helper(s, len_s - k + 1)
