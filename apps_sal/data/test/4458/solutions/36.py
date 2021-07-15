n = int(input())
a = list(map(int,input().split()))
count = 0
mina = n + 1
for i in a:
    if mina >= i:
        count += 1
        mina = i

print(count)
