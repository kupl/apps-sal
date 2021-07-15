
n = int(input())
s = input()

cur = 0

for ch in s:

    if ch == '(':
        cur += 1
    else:
        cur -= 1
    
    if cur == -2:
        print("No")
        return

print("Yes" if cur == 0 else "No")
