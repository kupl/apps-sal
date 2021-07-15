H, W = map(int, input().split())

def case1(h, w):
    MIN = float('inf')
    for i in range(1, h):
        sa = i * w
        sb = (h - i) * (w//2)
        sc = (h - i) * (w - w//2)
        if max([sa,sb,sc]) - min([sa,sb,sc]) < MIN:
            MIN = max([sa,sb,sc]) - min([sa,sb,sc]) 
    return MIN

def case2(h, w):
    MIN = float('inf')
    for i in range(1, h):
        sa = i * w
        sb = (h - i)//2 * w
        sc = (h - i -(h - i)//2) * w
        if max([sa,sb,sc]) - min([sa,sb,sc]) < MIN:
            MIN = max([sa,sb,sc]) - min([sa,sb,sc]) 
    return MIN
print(min([case1(H,W) , case1(W,H), case2(H,W), case2(W,H)]))
