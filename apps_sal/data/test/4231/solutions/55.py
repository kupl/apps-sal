H, W = map(int, input().split(" "))
h, w = map(int, input().split(" "))


black = H * w + W * h - h * w

print(H * W - black)
