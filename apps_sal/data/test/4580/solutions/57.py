def color(n):
    if n < 400:
        return '灰'
    elif n < 800:
        return '茶'
    elif n < 1200:
        return '緑'
    elif n < 1600:
        return '水'
    elif n < 2000:
        return '青'
    elif n < 2400:
        return '黄'
    elif n < 2800:
        return '橙'
    elif n < 3200:
        return '赤'
    else:
        return None


N = int(input())
a = list(map(int, input().split()))
colors = set()
over = 0
for c in a:
    if color(c):
        colors.add(color(c))
    else:
        over += 1
print(max(1, len(colors)), end=' ')
print(len(colors) + over)
