

def process():
    li = list(input())
    x = int(input())
    n = len(li)
    ans = ['1' for i in range(n)]

    for i in range(0, n):
        if(li[i] == '0'):
            if(i - x >= 0):
                ans[i - x] = '0'
            if(i + x < n):
                ans[i + x] = '0'

    for i in range(0, n):
        chr = '0'
        if(i - x >= 0 and ans[i - x] == '1'):
            chr = '1'
        if(i + x < n and ans[i + x] == '1'):
            chr = '1'
        if(li[i] == chr):
            pass
        else:
            print(-1)
            return
    print("".join(ans))


tests = int(input())
for i in range(tests):
    process()
