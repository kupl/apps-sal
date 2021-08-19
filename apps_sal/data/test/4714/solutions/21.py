lst = input().split()
count = 0


def judge(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


for i in range(int(lst[0]), int(lst[1]) + 1):
    if judge(i):
        count += 1
print(count)
