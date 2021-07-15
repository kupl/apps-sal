H, W = map(int, input().split())
A = [input() for _ in range(H)]

W += 2
f = '#'
print(f * W)
for a in A:
    print(f'#{a}#')
print(f * W)
