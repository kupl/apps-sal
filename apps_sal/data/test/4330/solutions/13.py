A, B = map(int, input().split())

if (A - B) % 2 != 0:
    K = 'IMPOSSIBLE'
else:
    K = (A + B) // 2

print(K)
