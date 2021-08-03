N = int(input())
S = input()
if N % 2 != 0:
    print("No")
else:
    if S[:N // 2] * 2 == S:
        print("Yes")
    else:
        print("No")
