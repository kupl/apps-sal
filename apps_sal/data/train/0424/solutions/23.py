class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        if N == 1:
            return 1 if img1[0][0] == 1 and img2[0][0] == 1 else 0
        max_slide = N
        sliders = set()
        for i in range(N):
            for j in range(N):
                sliders.add((i, j))
                sliders.add((-i, j))
                sliders.add((i, -j))
                sliders.add((-i, -j))
        
        def slide_and_count(slide):
            res = 0
            left, down = slide
            for i in range(min(N, N-left)):
                i2 = i + left
                for j in range(min(N, N-down)):
                    j2 = j + down
                    if i2 < 0 or j2 < 0:
                        continue
                    try:
                        if img1[i][j] == 1 and img2[i2][j2] == 1:
                            res += 1
                    except:
                        pass
                    
            print(slide, res)
            return res
        
        return max(slide_and_count(slide) for slide in sliders)
