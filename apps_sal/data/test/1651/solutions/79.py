S, P = map(int, input().split())
for i in range(1, int(P**0.5) + 1):
    if i * (S - i) == P:
        print("Yes")
        return
print("No")
