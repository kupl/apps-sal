from collections import Counter


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        # if len(A)%2==1:
        #     return False
        # counter = Counter(A)
        # # print(counter)
        # Skey = set(counter.keys())
        # key = counter.keys()
        # for i in key:
        #     if 2*i in Skey:
        #         counter[i]=0
        #         counter[i*2]-=counter[i]
        # val = list(counter.values())
        # print(val)
        # for i in val:
        #     if i !=0:
        #         return False
        # return True

        cnt = collections.Counter(A)
        for a in sorted(A, key=abs):
            if cnt[a] and cnt[a * 2]:
                cnt[a] -= 1
                cnt[a * 2] -= 1
        return all(cnt[a] == 0 for a in A)
