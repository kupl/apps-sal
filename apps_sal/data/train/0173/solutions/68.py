class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        tmp = collections.Counter()
        for x in arr:
            tmp[x % k] += 1
        for c, v in list(tmp.items()):
            if c == 0 and v % 2 != 0:
                return False
            elif c != 0 and v != tmp[k - c]:
                return False
        return True
# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         mod = [0] * k
#         for num in arr:
#             mod[num % k] += 1
#         print(mod)
#         if any(mod[i] != mod[k - i] for i in range(1, k // 2)):
#             return False
#         return mod[0] % 2 == 0

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k/solution/jian-cha-shu-zu-dui-shi-fou-ke-yi-bei-k-zheng-chu-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
