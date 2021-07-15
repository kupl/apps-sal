n = int(input())
u = []
for _ in range(n):
       inp = input()
       if inp in u:
              print('YES')
       else:
              u.append(inp)
              print('NO')
