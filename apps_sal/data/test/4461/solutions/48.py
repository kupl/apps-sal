(h, w) = list(map(int, input().split()))
if h % 3 == 0 or w % 3 == 0:
    print(0)
else:
    num1 = max(h // 3 * w, (h - h // 3) * (w // 2), (h - h // 3) * (w - w // 2)) - min(h // 3 * w, (h - h // 3) * (w // 2), (h - h // 3) * (w - w // 2))
    num2 = max(w // 3 * h, (w - w // 3) * (h // 2), (w - w // 3) * (h - h // 2)) - min(w // 3 * h, (w - w // 3) * (h // 2), (w - w // 3) * (h - h // 2))
    num3 = max((h // 3 + 1) * w, (h - (h // 3 + 1)) * (w // 2), (h - (h // 3 + 1)) * (w - w // 2)) - min((h // 3 + 1) * w, (h - (h // 3 + 1)) * (w // 2), (h - (h // 3 + 1)) * (w - w // 2))
    num4 = max((w // 3 + 1) * h, (w - (w // 3 + 1)) * (h // 2), (w - (w // 3 + 1)) * (h - h // 2)) - min((w // 3 + 1) * h, (w - (w // 3 + 1)) * (h // 2), (w - (w // 3 + 1)) * (h - h // 2))
    print(min(num1, num2, num3, num4, h, w))
