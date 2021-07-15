a, b = list(map(int, input().split()))
curr = 1
while True:
    if curr % 2 == 1:
        a -= curr
    if curr % 2 == 0:
        b -= curr
    curr += 1
    if a < 0:
        print("Vladik")
        return
    if b < 0:
        print("Valera")
        return

