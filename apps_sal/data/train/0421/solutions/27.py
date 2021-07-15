class Solution:
    def lastSubstring(self, s: str) -> str:
        
        step = 0
        index = [i for i in range(len(s))]

        biggest_letter = 'a'
        for i in index:
            if s[i + step] > biggest_letter:
                biggest_letter = s[i + step]

        buff_index = []
        for i in index:
            if (s[i + step] == biggest_letter) & (i + step < len(s)):
                if i==0:
                    buff_index.append(i)
                if  ((i!=0) and (s[i-1]!=s[i])):
                    buff_index.append(i)
        index = buff_index
        step += 1


        while (len(index) > 1):
            biggest_letter = 'a'
            for i in index:
                if i+step < len(s):
                    if s[i+step] > biggest_letter:
                        biggest_letter = s[i+step]

            buff_index = []
            for i in index:
                if i + step < len(s):
                    if (s[i+step] == biggest_letter) & (i+step<len(s)):
                        buff_index.append(i)

            index = buff_index

            step += 1


        res = s[index[0]:len(s)]

        return res
