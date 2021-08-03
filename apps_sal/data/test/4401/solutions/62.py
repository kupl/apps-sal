def resolve():
    x, y, z = map(int, input().split())
    x, y = y, x
    x, z = z, x
    print(f'{x} {y} {z}')


resolve()
