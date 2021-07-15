A = input()
B = input()

print("YES" if A[0] == B[-1] and A[-1] == B[0] and A[1] == B[1] else "NO")
