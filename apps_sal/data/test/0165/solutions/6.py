def get(x, y, z):
    return max(x, y, z) * 3 - x - y - z


a, b, c = list(map(int, input().split()))
ans = min(get(a, b, c),
          get(a - 1, b, c),
          get(a - 1, b - 1, c),
          get(a, b - 1, c),
          get(a, b - 1, c - 1),
          get(a, b, c - 1),
          get(a - 1, b, c - 1),
          )
print(ans)
