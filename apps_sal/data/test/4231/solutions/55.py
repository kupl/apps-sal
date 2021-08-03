H, W = map(int, input().split(" "))
h, w = map(int, input().split(" "))

# print(H,W)
# print(h,w)

black = H * w + W * h - h * w

print(H * W - black)
