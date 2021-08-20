class Solution:

    def lastSubstring(self, s: str) -> str:
        st = set()
        for l in s:
            st.add(l)
        if len(st) == 1:
            return s
        largest_letter = sorted(list(st))[-1]
        nums = []
        for (index, letter) in enumerate(s):
            if letter == largest_letter:
                nums.append(index)
        rez = s[nums[0]:]
        og_first = nums[0]
        for i in nums[1:]:
            first = og_first
            (second, j) = (i, i)
            while second < len(s):
                if s[first] == s[second]:
                    first += 1
                    second += 1
                elif s[first] > s[second]:
                    break
                elif s[first] < s[second]:
                    rez = s[j:]
                    og_first = j
                    break
        return rez
