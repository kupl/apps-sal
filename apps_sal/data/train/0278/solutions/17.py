class Solution:

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dic = defaultdict(list)
        for d in digits:
            dic[d % 3].append(d)
        arr = []
        n1 = len(dic[1])
        n2 = len(dic[2])
        arr += dic[0]
        if n1 % 3 == n2 % 3 == 0 or n1 == n2:
            arr += dic[1] + dic[2]
        else:
            dic[1].sort(reverse=1)
            dic[2].sort(reverse=1)
            l1 = l2 = 0
            if n1 % 3 == 2 and n2 == 3:
                while n2 > 3:
                    l2 += 3
                    n2 -= 3
                l1 += n1 // 3 * 3
                l1 += 2
                l2 += 2
            elif n2 % 3 == 2 and n1 == 3:
                while n1 > 3:
                    l1 += 3
                    n1 -= 3
                l2 += n2 // 3 * 3
                l2 += 2
                l1 += 2
            else:
                if n1 > 2:
                    l1 += n1 // 3 * 3
                    n1 -= n1 // 3 * 3
                if n2 > 2:
                    l2 += n2 // 3 * 3
                    n2 -= n2 // 3 * 3
                if n1 != 0 and n2 != 0:
                    min1 = min(n1, n2)
                    l1 += min1
                    l2 += min1
            arr += dic[1][:l1] + dic[2][:l2]
        arr.sort(reverse=1)
        if arr and arr[0] == 0:
            return '0'
        return ''.join((str(i) for i in arr))
