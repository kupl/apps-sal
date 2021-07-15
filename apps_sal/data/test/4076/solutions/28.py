import math
A, B, H, M = map(int, input().split())
sitaH = (H*60+M) / 720 * 2 * math.pi
sitaM =  M/60 * 2 * math.pi

posXH = A * math.cos(sitaH)
posYH = A * math.sin(sitaH)
posXM = B * math.cos(sitaM)
posYM = B * math.sin(sitaM)

delX = posXH - posXM
delY = posYH - posYM

d = (delX*delX + delY*delY)**(1/2)
print(d)
