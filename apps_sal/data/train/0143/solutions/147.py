class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        '''
        行不通的 example4就不满足
        from collections import Counter
        n = len(tree)
        record = []

        for i in range(n):
            a = len(Counter(tree[:i+1]))
            record.append(a)
        print(record)
        dic = {}
        ans = 0
        dic[0] = [-1,-1] 
        for i in range(n):
            if record[i] not in dic.keys():
                dic[record[i]] = [i,i]
            else:
                dic[record[i]][1] = i

            if record[i]-2 in dic.keys():
                print(i,dic[record[i]],dic[record[i]-2])
                ans = max(ans,dic[record[i]][1]-dic[record[i]-2][1])
                print('ans=',ans)


        return ans
        '''
        n = len(tree)
        dic = {}
        x = 0
        for i in range(n):
            if tree[i] not in dic.keys():
                dic[tree[i]] = 1
            else:
                dic[tree[i]] += 1

            if len(dic) > 2:
                dic[tree[x]] -= 1
                if dic[tree[x]] == 0:
                    del dic[tree[x]]
                x += 1
        return i - x + 1
