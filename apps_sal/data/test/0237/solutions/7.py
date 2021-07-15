

def pillows_needed(height, width):
    if height > width:
        return height * (height + 1) // 2 - (height - width) * (height - width + 1) // 2
    else:
        return height * (height + 1) // 2 + (width - height)

n, m, k = list(map(int, input().split()))


a, b, c = 0, m, 0

while a < b:
    c = (a + b + 1) // 2
    if m >= c + pillows_needed(c - 1, n - k) + pillows_needed(c - 1, k - 1):
        a = c
    else:
        b = c - 1

print(a)

