N = int(input())
for a in range(1, 38):
    for b in range(1, 26):
        if 3**a + 5**b == N:
            print(a, b)
            return
print(-1)
