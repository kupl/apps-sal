abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = int(input())
S = input()

ans = []
for c in S:
    print(abc[(abc.index(c) + N) % len(abc)], end="")
