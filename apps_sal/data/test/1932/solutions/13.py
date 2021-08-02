n = int(input())

cnt = {"Tetrahedron": 4,
       "Cube": 6,
       "Octahedron": 8,
       "Dodecahedron": 12,
       "Icosahedron": 20}

ans = 0
for i in range(n):
    name = input()
    ans += cnt[name]

print(ans)
