n = int(input())
for i in range(n):
    inp = input().split()
    if 2400 <= int(inp[1]) < int(inp[2]):
        print('YES')
        break
else:
    print('NO')
