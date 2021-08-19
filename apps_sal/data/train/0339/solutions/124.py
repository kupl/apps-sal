class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        self.ans = 0

        def func(n1, n2):
            for prod in n1:
                i, j = 0, len(n2) - 1
                while i < j:
                    if n2[i] == n2[j]:
                        if n2[i] * n2[j] != prod * prod:
                            break
                        n = j - i + 1
                        self.ans += (n * (n - 1)) // 2
                        # print(self.ans)
                        break
                    #print(n2, i, j, prod*prod, n2[i], n2[j], n2[i]*n2[j])
                    if n2[i] * n2[j] == prod * prod:
                        temp = n2[i]
                        t1, t2 = 0, 0
                        while i < j and n2[i] == temp:
                            t1 += 1
                            i += 1
                        temp = n2[j]
                        while i <= j and n2[j] == temp:
                            t2 += 1
                            j -= 1
                        self.ans += (t1 * t2)
                    elif n2[i] * n2[j] > prod * prod:
                        j -= 1
                    else:
                        i += 1
        nums1.sort()
        nums2.sort()
        func(nums1, nums2)
        # print(self.ans)
        func(nums2, nums1)
        return self.ans
