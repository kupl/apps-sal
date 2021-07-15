class Solution:
    def knightDialer(self, n: int) -> int:
        h = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        if n == 1:
            return 10
        
        o = []
        le = 0
        
        oTrack = [0] * 10
        track = [0] * 10
        
        for loops in range(n - 1):
            track = [0] * 10
            for k,v in enumerate(track):
                #print(\"k: \", k, track)
                hg = h.get(k)
                for i in hg:
                    track[i] += max(oTrack[k], 1)
                    
            
            #print(\"loop: \", loops, p, track, oTrack)
            oTrack = track.copy()
            
        
        return sum(track) % (10 ** 9 + 7)

