N = int(input())
S = []
while N:
    N -= 1
    S.append(chr(97 + N % 26))
    N //= 26
print("".join(S[::-1]))
