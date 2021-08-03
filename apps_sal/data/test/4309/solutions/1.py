n = int(input())

while True:
    n = str(n)
    if n[0] == n[1] == n[2]:
        break
    n = int(n) + 1
print(n)
