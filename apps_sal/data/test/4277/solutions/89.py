N, A, B = map(int, input().split())

# N人*A円がB円より大きい場合
if N * A > B:
    print(B)
else:
    print(N * A)
