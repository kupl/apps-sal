"""
KA      YM        KA        AS      KA  ASKA      YASK        KA         SKAYMA   
KA    KA         SKAY        SK    SK   AS AY    AY SK       SKAY       AS    AS  
KA  AS          AS  YM        KA  AS    AS  YM  KA  SK      AS  YM      AS        
KAYM           MA    MA        AYMA     AS   MASK   SK     MA    MA      SKAYMA   
KA  AS        YMASKAYMAS        YM      AS    AS    SK    YMASKAYMAS          AS  
KA    KA     AY        SK       YM      AS          SK   AY        SK   AS    AS  
KA      YM  KA          KA      YM      AS          SK  KA          KA   SKAYMA   
"""
n = int(input())
for i in range(n):
    (x, y, k) = map(int, input().split())
    (x, y) = (abs(x), abs(y))
    min_moves = max(x, y)
    if min_moves > k:
        print(-1)
    else:
        ans = min(x, y)
        x -= ans
        y -= ans
        p = max(x, y)
        k -= ans
        if k == p and p % 2 == 0:
            print(ans + k)
        elif k == p and p % 2 == 1:
            print(ans + k - 1)
        elif p % 2 == 0 and k % 2 == 0:
            print(ans + k)
        elif p % 2 == 0 and k % 2 == 1:
            print(ans + k - 2)
        elif p % 2 == 1:
            print(ans + k - 1)
