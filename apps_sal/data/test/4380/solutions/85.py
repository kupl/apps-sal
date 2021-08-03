A, B = map(int, input().split())

if A % 2 == 1:
    if B % 2 == 1:
        print("Yes")
        return

print("No")
