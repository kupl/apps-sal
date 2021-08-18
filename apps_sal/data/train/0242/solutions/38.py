class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:

        hashtable = {}
        hashcount = {}
        m = 0

        for i in range(len(nums)):

            if nums[i] not in list(hashtable.keys()):
                hashtable[nums[i]] = 1
                if 1 not in list(hashcount.keys()):
                    hashcount[1] = [nums[i]]
                else:
                    hashcount[1].append(nums[i])
            else:
                c = hashtable[nums[i]]
                hashtable[nums[i]] += 1

                hashcount[c].remove(nums[i])
                if len(hashcount[c]) == 0:
                    del hashcount[c]
                if c + 1 in list(hashcount.keys()):
                    hashcount[c + 1].append(nums[i])
                else:
                    hashcount[c + 1] = [nums[i]]

            if (len(list(hashtable.keys())) == 1):
                m = i + 1

            else:
                l = list(hashcount.keys())

                if (len(l) == 1 and l[0] == 1):
                    m = max(m, i + 1)
                if len(list(hashcount.keys())) == 2:
                    if 1 in list(hashcount.keys()) and len(hashcount[1]) == 1:
                        m = max(m, i + 1)
                    if abs(l[0] - l[1]) == 1 and len(hashcount[max(l[0], l[1])]) == 1:
                        m = max(m, i + 1)

        return m
