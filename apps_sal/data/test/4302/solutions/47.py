A, B = map(int, input().split())

# 以下を出力する
# A > B => A + (A − 1)
# A < B => B + (B − 1)
# A = B => A + B
if A > B:
    print(2 * A - 1)
elif A == B:
    print(A + B)
else:
    print(2 * B - 1)
