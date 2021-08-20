(vertical1, horizontal1, vertical2, horizontal2) = map(int, input().split())
if vertical1 * horizontal1 < vertical2 * horizontal2:
    print(vertical2 * horizontal2)
else:
    print(vertical1 * horizontal1)
