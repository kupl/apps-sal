H, W = map(int, input().split())
h, w = map(int, input().split())
t = H * W
o = h * W + w * H
c = h * w
diff = o - c
print(t - diff)
