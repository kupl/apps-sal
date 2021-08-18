def input2():
    return map(int, input().split())


H, W = input2()
h, w = input2()

ans = (H - h) * (W - w)
print(ans)
