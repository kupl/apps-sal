(w, h, x, y) = map(int, input().split())
print(f'{w * h / 2} {(1 if (x * 2, y * 2) == (w, h) else 0)}')
