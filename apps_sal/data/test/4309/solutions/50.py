n = str(input())
for i in ['111', '222', '333', '444', '555', '666', '777', '888', '999']:
    if i == n:
        print(n)
        break
    elif n < i:
        print(i)
        break
