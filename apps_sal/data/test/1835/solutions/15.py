q = int(input())
for i in range(q):
    amount = 0
    n = int(input())
    flag = 0
    for j in range(n):
        s = input()
        for k in range(len(s)):
            if s[k] == '1':
                amount += 1
        if len(s) % 2:
            flag = 1
   # print(flag, amount)
    if not flag and amount % 2:
        print(n - 1)
    else:
        print(n)

