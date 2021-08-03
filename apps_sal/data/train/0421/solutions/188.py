class Solution:  # 双指针
    def lastSubstring(self, s: str) -> str:
        left = 0  # 代表以left为起始点的字串
        right = 1
        step = 0
        while (right + step) < len(s):
            if s[left + step] < s[right + step]:
                left = right
                right += 1
                step = 0
            elif s[left + step] == s[right + step]:
                step += 1
            else:
                right += step + 1
                step = 0
        return s[left:]


# 使用指针left记录当前最大的后缀子串的起始坐标。 指针right用来遍历。 一开始left = 0， right = 1，从左往右遍历。
# 当str[left] 小于 str[right], 则以left开头的后缀子串一定小于以right开头的后缀子串，所以left = right， right+1
# 当str[left] 大于 str[right], 则left不动，right+1
# 当str[left] 等于 str[right]， 则比较str[left + k], str[right + k], k = 1、2、3...。 直到出现不相等，否则一直比较直到结束。
# 当str[left + k] 小于 str[right + k]， left = right, right+1
# 当str[left + k] 大于于 str[right + k]， left不动, right+step+1。
