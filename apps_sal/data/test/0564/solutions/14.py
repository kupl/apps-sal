n, s = list(map(int, input().split()))
krush = list(map(int, input().split()))
chasha = 0
res = 'YES'
krush.sort()
friend = 0
while res == 'YES' and friend < len(krush) - 1:
    chasha += krush[friend]
    if chasha > s:
        res = 'NO'
    friend += 1
print(res)
