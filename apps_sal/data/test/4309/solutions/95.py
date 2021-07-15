N = int(input())
for i in range(1,10):
    if 111*i >=N and N > 111*(i-1):
        print(111*i)
        return
