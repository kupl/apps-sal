class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue
                if ageA < 100 < ageB:
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA

        return ans


'''
不考虑遍历所有的 20000 个人，我们只考虑遍历所有的元组 (age, count) 表示在这个年纪有多少人。因为最多只有 120 个可能的年纪，这会是一个很快的提升。

算法

对于每个元组 (ageA, countA)，(ageB, countB)，如果条件满足对应的年纪，那么久将 countA * countB 加入发好友请求的人数。

当 ageA == ageB 的时候我们就数多了：我们只有 countA * (countA - 1) 对好友请求，因为你不能和自己发送请求。

JavaPython



'''
