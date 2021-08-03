N = int(input())
src = [input() for i in range(N)]
src.sort(key=lambda x: len(x))

for a, b in zip(src, src[1:]):
    if a in b:
        continue
    print('NO')
    return
print('YES')
for a in src:
    print(a)
