n = int(input())
inStr = input()

pos = [int(x) for x in inStr.split()]
min = n
ans = 0
for i in range(n - 1, -1, -1):
    if pos[i] > min:
        ans = i + 1
        break
    elif pos[i] < min:
        min = pos[i]

print(ans)
