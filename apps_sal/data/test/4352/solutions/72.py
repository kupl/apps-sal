# 054a

A, B = list(map(int, input().split()))    # カードの数字を入力

if A == B:
    print("Draw")
elif A == 1:
    print("Alice")
elif B == 1:
    print("Bob")
elif A < B:
    print("Bob")
else:
    print("Alice")
