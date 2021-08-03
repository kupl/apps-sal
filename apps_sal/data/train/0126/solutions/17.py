from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        mx_count = 0

        def create_dct(size, mx_count):
            dct = defaultdict(int)

            i = 0
            j = size - 1

            while j < len(s):

                temp = []
                temp_dict = defaultdict(int)

                flag = True
                for x in range(i, j + 1):
                    temp.append(s[x])
                    temp_dict[s[x]] += 1
                    if len(temp_dict) > maxLetters:
                        flag = False
                        break

                i += 1
                j += 1

                if not flag:
                    continue

                tmp_string = ''.join(temp)
                dct[tmp_string] += 1

                if dct[tmp_string] > mx_count:
                    mx_count = dct[tmp_string]

            return mx_count

        mx_count = create_dct(minSize, mx_count)
        mx_count = max(create_dct(maxSize, mx_count), mx_count)

        return mx_count
