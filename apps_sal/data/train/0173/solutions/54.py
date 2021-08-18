class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hashtable = dict()
        count = 0
        for x in arr:
            corresp = abs(k - x % k)
            if corresp in hashtable:
                if k - corresp == corresp:
                    if hashtable[corresp] == 1:
                        hashtable[corresp] = 0
                    else:
                        hashtable[corresp] = 1
                else:
                    hashtable[corresp] -= 1
            elif k - corresp in hashtable:
                if k - corresp != 0:
                    hashtable[k - corresp] += 1
                else:
                    hashtable[k - corresp] = 0
            else:
                hashtable[k - corresp] = 1
        print(count)

        for x in hashtable:
            if hashtable[x] != 0:
                print(x, hashtable[x])
                return False

        return True
