# A - ι⊥l

# b-a = c-bを満たしていればYes, そうでなければNoを出力する


a, b, c = list(map(int, input().split()))

if b - a == c - b:
    print('YES')
else:
    print('NO')
