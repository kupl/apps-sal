N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))
first_val = sorted(ls, reverse=True)[0]
second_val = sorted(ls, reverse=True)[1]
for i in ls:
    if i == first_val:
        print(second_val)
    else:
        print(first_val)
