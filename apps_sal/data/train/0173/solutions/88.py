class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # 余数字典
        d = {i:0 for i in range(k)}
        # 求每个值的余数，并统计个数
        for num in arr:
            d[num % k] += 1
        # 若正好除尽的个数为奇数，证明除不尽的为奇数个，无法形成pair
        if d[0] % 2 != 0:
            return False
        for i in range(1, k):
            # 此处有一个trick，若两个数余数相加为k,则这两个数的和可以被k整除（相当于多加了一个k），所以如果出现频率相等，这两组数即可两两配对
            if i != k-i:
                if d[i] != d[k-i]:
                    return False
            else:
                if d[i] % 2 != 0:
                    return False
        
        return True
