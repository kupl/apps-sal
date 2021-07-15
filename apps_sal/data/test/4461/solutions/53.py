#!/usr/bin/env python3


def main():
    H, W = list(map(int, input().split()))
    if H % 3 == 0 or W % 3 == 0:
        print((0))
    else:
        ans = min(W,H)

        # Hを1:2で分割
        for i in range(3):
            d = (H // 3)- 1 + i
            if d > 0:
                choco = [d * W, (H-d) * (W//2), (H-d) * (W - W//2)]
                ans = min(ans, max(choco) - min(choco))
        
        # Wを1:2で分割
        for i in range(3):
            d = (W // 3)- 1 + i
            if d > 0:
                choco = [d * H, (W-d) * (H//2), (W-d) * (H - H//2)]
                ans = min(ans, max(choco) - min(choco))
        
        print(ans)


def __starting_point():
    main()

__starting_point()
