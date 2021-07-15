class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        vals = {0 : 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        total = 0
        res = []
        for digit in digits:
            vals[digit] += 1
            total += int(digit)
        if total % 3 == 0:
            temp = 0
            for i in range(9,0,-1):
                temp += vals[i]
            if temp == 0:
                return '0'
            for i in range(9,-1,-1):
                for _ in range(vals[i]):
                    res.append(str(i))
            return ''.join(res)
        
        if total % 3 == 1:
            for i in range(10):
                if i%3 == 1 and vals[i] > 0:
                    vals[i] -= 1
                    for i in range(9,-1,-1):
                        for _ in range(vals[i]):
                            res.append(str(i))
                    return ''.join(res)
            count = 0
            i = 0
            while i < 10:
                if count == 2:
                    for i in range(9,-1,-1):
                        for _ in range(vals[i]):
                            res.append(str(i))
                    return ''.join(res)
                elif i%3 == 2 and vals[i] > 0:
                    vals[i] -= 1
                    count += 1
                else:
                    i += 1
        else:
            for i in range(10):
                if i%3 == 2 and vals[i] > 0:
                    vals[i] -= 1
                    for i in range(9,-1,-1):
                        for _ in range(vals[i]):
                            res.append(str(i))
                    return ''.join(res)
            count = 0
            i = 0
            while i < 10:
                if count == 2:
                    for i in range(9,-1,-1):
                        for _ in range(vals[i]):
                            res.append(str(i))
                    return ''.join(res)
                elif i%3 == 1 and vals[i] > 0:
                    vals[i] -= 1
                    count += 1
                else:
                    i += 1
                    
                        
                    
        return ''.join(res)

