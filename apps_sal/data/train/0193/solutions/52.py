class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = {}
        for num in arr:
            dic[num] = dic.get(num, 0) + 1

        array = [v for k, v in sorted(list(dic.items()), key=lambda item: item[1], reverse=True)]

        target = len(arr) / 2

        current, i = 0, 0
        for num in array:
            i += 1
            current += num
            if current >= target:
                return i
