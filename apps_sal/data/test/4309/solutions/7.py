N = int(input())

ans = ''
for i in range(1, 10):
    ans = str(i) * 3
    if int(ans) >= N:
        print(int(ans))
        return
