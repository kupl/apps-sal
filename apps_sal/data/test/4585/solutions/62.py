x = int(input())

# 1, 2, 3, ... , nの総和がX以上ならば、
# 適当に保持をいれることでたどり着ける
# 総和の公式は(1 + n)*n//2

ans = 0
while True:
    if ((1+ans)*ans)//2 >= x:
        print(ans)
        return
    ans+=1
