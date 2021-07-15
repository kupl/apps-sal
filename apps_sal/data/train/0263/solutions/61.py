class Solution:
    def knightDialer(self, n: int) -> int:
        dirs = {(-2, -1), (-1, -2), (1, -2), (2, -1),
                (2, 1), (1, 2), (-1, 2), (-2, 1)}
        prohibited = {(0, 3), (2, 3)}
        
        graph = {}
        result = [0] * (3 * 4)
        for i in range(3 * 4):
            x1 = i % 3
            y1 = i // 3
            graph[i] = []
            if (x1, y1) in prohibited:
                continue
            
            for j in range(3 * 4):
                x2 = j % 3
                y2 = j // 3

                if (x2 - x1, y2 - y1) in dirs and (x2, y2) not in prohibited:
                    graph[i].append(j)
            result[i] = 1
            
        # for k, v in graph.items():
        #     print(k, v)
        M = 10 ** 9 + 7
        for i in range(1, n):
            res_next = [0] * (3 * 4)
            for x in range(3 * 4):
                for adj in graph.get(x, []):
                    res_next[x] = (res_next[x] + result[adj]) % M
                    
            result = res_next
        # print(result)
        return sum(result) % M
