class Solution:
    def knightDialer(self, n: int) -> int:
        '''
        0->[4,6]->[1,3,7,9]->
        
        2 20 (3, 6), (2, 14)
        
        '''
        if n == 1: return 10
        
        m = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        cnt = defaultdict(int)
        for k in m:
            for v in m[k]:
                cnt[v] += 1
        
        for _ in range(n-2):
            cnt2 = defaultdict(int)
            for k in cnt:
                for v in m[k]:
                    cnt2[v] += cnt[k]
            cnt = cnt2
        
        return sum(cnt[k] for k in cnt) % (10**9+7)
