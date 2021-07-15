n = int(input())
for i in range(n):
    s = input().split()
    b = int(s[1])
    e = int(s[2])
    if b >= 2400 and e > b:
        print("YES")
        return
print('NO')

