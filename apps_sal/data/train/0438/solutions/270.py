# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         #两个数组，一个记录长度，另一个记录长度的个数
#         length = [0 for _ in range(len(arr)+2)]
#         count = [0 for _ in range(len(arr)+1)]
#         res = -1
#         for i, a in enumerate(arr):
#             #先把左边的长度和右边的1长度取出来
#             left, right = length[a-1], length[a+1]
#             #现在这个位置的长度就是左边的长度加上右边的长度加上自己
#             #距离a位置的左右两边的边角处的索引也会被附上新的值，之后的计算可能用得上
#             length[a] = length[a-left] = length[a+right] = left + right + 1
            
#             #然后就是更新count了
#             count[left] -= 1
#             count[right] -= 1
#             count[length[a]] += 1
            
#             #判断m是否还存在，只要m存在那就是满足条件的最后一步
#             if count[m]:
#                 res = i+1
#         return res

class UnionFindSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)] #表示index位置的1的长度

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        #作为父亲节点的条件，谁的长度比较大。就跟着谁。 如果长度相同时会不会有问题? 感觉这里写得不对，长度相同时应该看pu和pv哪个比较大(小). 也许按长度来作为父亲节点并没有影响，也可以尝试找索引值较小的元素作为父亲节点
        # if self.ranks[pu] > self.ranks[pv]:
        #     self.parents[pv] = self.parents[pu]
        #     self.ranks[pu] += self.ranks[pv] #这里只修改pu的1长度原因是，以后查询pv的长度都会指向pu的长度
        # else:
        #     self.parents[pu] = self.parents[pv]
        #     self.ranks[pv] += self.ranks[pu]
        self.parents[max(pu,pv)] = min(pu, pv)
        self.ranks[min(pu,pv)] += self.ranks[max(pu,pv)]
             
        return True
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m: #最后一步
            return m
        
        uf = UnionFindSet(len(arr))
        n, ans = len(arr), -1
        
        for step, a in enumerate(arr):
            a -= 1 #字符串索引从0开始
            
            uf.ranks[a] = 1
            #找左右节点进行联结
            for j in (a-1, a+1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        #上一步还存在m长度的1群. 也许在其他地方还有存在m长度的，但是后面会遍历到. 注意这里遍历不到最后一步
                        ans = step
                    #如果j位置上是1,即1的群长度大于0。 则可以进行连接
                    if uf.ranks[j] > 0:
                        uf.union(a , j)
                        
        return ans
