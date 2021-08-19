a = int(input())
b = int(input())
h = int(input())
if (1 <= a & a <= 100) & (1 <= b & b <= 100) & (1 <= h & h <= 100):
    if h % 2 == 0:
        s = int((a + b) * h / 2)
        print(s)
