h, w = map(int, input().split())

p1 = [(h//3) * w, (h//3) * w, (h-2*(h//3))*w]
p2 = [(w//3) * h, (w//3) * h, (w-2*(w//3))*h]
p3 = [(h//3) * w, (h - h//3)* (w//2), h*w - (h//3) * w - (h - h//3)* (w//2)]
p4 = [(w//3) * h, (w - w//3)* (h//2), h*w - (w//3) * h - (w - w//3)* (h//2)]

p5 = [(h//3 + 1) * w, (h//3 + 1) * w, (h-2*(h//3 + 1))*w]
p6 = [(w//3 + 1) * h, (w//3 + 1) * h, (w-2*(w//3 + 1))*h]
p7 = [(h//3 + 1) * w, (h - h//3 - 1)* (w//2), h*w - (h//3 + 1) * w - (h - h//3 - 1)* (w//2)]
p8 = [(w//3 + 1) * h, (w - w//3 - 1)* (h//2), h*w - (w//3 + 1) * h - (w - w//3 - 1)* (h//2)]

print(min(max(p1)-min(p1), max(p2)-min(p2), max(p3)-min(p3), max(p4)-min(p4), max(p5)-min(p5), max(p6)-min(p6), max(p7)-min(p7), max(p8)-min(p8)))
