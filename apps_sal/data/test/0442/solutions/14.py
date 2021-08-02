r = int(input())

if (r < 5 or r % 2 == 0):
    print("NO")
    return

print(1, (r - 3) // 2)
