class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # 7  -> 16  7, 22, 11, 34, 17, 52, 26, 133, 40, 20, 10, 5, 16, 8, 4, 2, 1 
        # 8  -> 3   8, 4, 2, 1 
        # 9  -> 19  9, 28, 14, 7, 22, 11, 34, 17,  
        # 10 -> 6   10, 5, 16, 8, 4, 2, 1
        # 11 -> 14  11, 34
        power_list = []
        d = {}
        for i in range(lo, hi+1):
            a = self.power(i, d)
            power_list.append(a)
        print(power_list)
        list2 = [i for i in range(lo, hi+1)]
        # [x for _, x in sorted(zip(Y,X), key=lambda pair: pair[0])]
        list2 = [ x for x, y in sorted(zip(list2, power_list), key = lambda x: x[1])]
        return list2[k-1]
        
    def power(self, x, dict1):
        if x in dict1:
            print(('hi', x))
            return dict1[x]
        else:
            orig = x
            list1 = []
            count = 0
            while x != 1 and x not in dict1:
                if x %2 == 0:
                    x /= 2
                else:
                    x = 3*x + 1
                x = int(x)
                count += 1
                list1.append(x)
            n = len(list1)
            if x == 1:
                dict1[orig] = n
                for elem in list1:
                    dict1[elem] = n-1
                    n -= 1
                
            else:
                print(('hi ', x))
                dict1[orig] = n+ dict1[x]
                for elem in list1:
                    dict1[elem] = n-1 + dict1[x]
                    n -= 1
            return dict1[orig]
            
                    

