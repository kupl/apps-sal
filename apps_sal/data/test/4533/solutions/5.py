class Solution:
 #     def findContentChildren(self, g, s):
 #         """
 #         :type g: List[int]
 #         :type s: List[int]
 #         :rtype: int
 #         """
 #         total = 1
 #         child_to_give = []
 #         child_index = 0
 #         s.sort()
 #         g.sort()
 #         for cookie in s:
 #             for child_greed in g:
 #                 print("child_greed " + str(child_greed))
 #                 print("cookie " + str(cookie))
 #                 if child_greed <= cookie:
 #                     if child_index not in child_to_give:
 #                         child_to_give.append(child_index)
 #                         g.remove(child_greed)

 #                 child_index += 1

 #         return len(child_to_give)

    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        total = 1
        child_to_give = []
        child_index = 0

        start_i = 0
        for j in range(0, len(g)):
            for i in range(start_i, len(s)):
                if s[i] >= g[j]:
                    child_to_give.append(j)
                    start_i = i + 1
                    break

        print(child_to_give)
        return len(child_to_give)

 #     def findContentChildrenSlow(self, g, s):
 #         """
 #         :type g: List[int]
 #         :type s: List[int]
 #         :rtype: int
 #         """
 #         s.sort()
 #         g.sort()
 #         total = 1
 #         child_to_give = []
 #         child_index = 0
 #         for child_greed in g:
 #             # Find children greed less than or equal to cookie value
 #             for cookie in s:
 #                 if child_greed <= cookie:
 #                     # print(cookie)
 #                     # print(child_greed)
 #                     if child_index not in child_to_give:
 #                         child_to_give.append(child_index)
 #                         # g.remove(child_greed)
 #                         s.remove(cookie)
 #                         # print(g)
 #                         # print(s)
 #                         # break
 #             child_index += 1

 #         return len(child_to_give)
 #         # return 2
