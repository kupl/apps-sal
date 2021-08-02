# 入力例は合うがWAになる

A = input()
B = input()


if A[0] == B[2] and A[1] == B[1] and A[2] == B[0]:
    print("YES")
else:
    print("NO")

# YESとNOにしないといけないところをYes、Noになっていた
