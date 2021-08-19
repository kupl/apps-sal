# 素直に全探索したほうが楽
H, W = (int(T) for T in input().split())
minSH = H * W
minSW = H * W
for TH in range(1, H):
    BlockA = TH * W

    if TH <= (H - 2):
        BlockB1 = ((H - TH) // 2) * W
        BlockC1 = H * W - (BlockA + BlockB1)
        BigSCa1 = max(BlockA, BlockB1, BlockC1)
        SmlSCa1 = min(BlockA, BlockB1, BlockC1)
        DifSCa1 = BigSCa1 - SmlSCa1
    else:
        DifSCa1 = H * W

    if W >= 2:
        BlockB2 = (H - TH) * (W // 2)
        BlockC2 = H * W - (BlockA + BlockB2)
        BigSCa2 = max(BlockA, BlockB2, BlockC2)
        SmlSCa2 = min(BlockA, BlockB2, BlockC2)
        DifSCa2 = BigSCa2 - SmlSCa2
    else:
        DifSCa2 = H * W

    if min(DifSCa1, DifSCa2) < minSH:
        minSH = min(DifSCa1, DifSCa2)

for TW in range(1, W):
    BlockA = H * TW

    if TW <= (W - 2):
        BlockB1 = H * ((W - TW) // 2)
        BlockC1 = H * W - (BlockA + BlockB1)
        BigSCa1 = max(BlockA, BlockB1, BlockC1)
        SmlSCa1 = min(BlockA, BlockB1, BlockC1)
        DifSCa1 = BigSCa1 - SmlSCa1
    else:
        DifSCa1 = H * W

    if H >= 2:
        BlockB2 = (H // 2) * (W - TW)
        BlockC2 = H * W - (BlockA + BlockB2)
        BigSCa2 = max(BlockA, BlockB2, BlockC2)
        SmlSCa2 = min(BlockA, BlockB2, BlockC2)
        DifSCa2 = BigSCa2 - SmlSCa2
    else:
        DifSCa2 = H * W

    if min(DifSCa1, DifSCa2) < minSW:
        minSW = min(DifSCa1, DifSCa2)

print(min(minSH, minSW))
