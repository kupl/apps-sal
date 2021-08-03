class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:

        hashtable = {}
        zero_count = 0
        for i in range(len(A)):
            if A[i] == 0:
                zero_count += 1
                continue
            if A[i] in list(hashtable.keys()):
                hashtable[A[i]] += 1

            else:
                hashtable[A[i]] = 1

        if zero_count % 2 == 1:
            return False
        else:
            key_list = []
            pair_count = 0
            for key in list(hashtable.keys()):
                key_list.append(key)

            key_list.sort()

            for key in key_list:
                if key % 2 == 0 and key // 2 in list(hashtable.keys()):
                    m = min(hashtable[key], hashtable[key // 2])
                    hashtable[key] -= m
                    hashtable[key // 2] -= m
                    pair_count += m

            if pair_count * 2 + zero_count == len(A):
                return True
            else:
                return False
