S, P = map(int, input().split())
for i in range(1, 10**7):
    if i * (S - i) == P:
        print("Yes")
        return
print("No")
