class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        # 法1. 一个很基础的想法是建立一个BST，每次里面取最小的，然后再依此把比他大的k-1个对应的value都减去1 O(N*lgN*k)

        # 法2. 可以先sort，然后简建立一个Counter, 从左到右遍历这个sort好的数组。这个适用于每个切片长度任意，至少为3的那道题。这道题也适用。这个方法主要是贪心思想。可以每次优先与之前的配对或者是一次性与后面三个配对。或者是与后面的k个配对。 O(N*logN)

        # 法3. 建立一个Counter。另外建立一个deque，把没有左节点的数字放进去。O(N)

        c = collections.Counter(nums)
        q = collections.deque()

        while c:

            # add new key in c:
            for key in c:
                if key - 1 not in c:
                    q.append(key)

            # iterate all of current roots
            while q:
                # print(q)

                cur = q.popleft()

                pushed = False

                for nxt in range(cur + 1, cur + k):
                    if c[nxt] < c[cur]:
                        return False

                    c[nxt] -= c[cur]

                    if c[nxt] == 0:
                        c.pop(nxt)

                    if not pushed and c[nxt] != 0:
                        pushed = True
                        q.append(nxt)

                c.pop(cur)

        return True if not c else False
