(x, y, z, w) = map(int, input().split())
print('Left' if x + y > z + w else 'Right' if x + y < z + w else 'Balanced')
