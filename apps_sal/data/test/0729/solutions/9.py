n = int(input())
# a = list(map(int,input().split()))
# m = int(input())
s = input()
f = s[0]
for c in s:
    if c != f:
        print('YES')
        print(f + c)
        return
print('NO')
