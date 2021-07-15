n, m = list(map(int, input().split()))

a = []
b = []

non_compressed = 0
compressed = 0
saves = []

for i in range(n):
    ai, bi = list(map(int, input().split()))
    non_compressed += ai
    compressed += bi
    saves.append(ai - bi)

if ( compressed > m ):
    print(-1)
else:
    saves.sort(reverse=True)
    z = 0
    while ( non_compressed > m ):
        non_compressed -= saves[z]
        z = z + 1
    print(z)

