N,K = list(map(int,input().split()))
log_ls = list(map(int,input().split()))

Max = max(log_ls)

def less_k(min_length,log_ls = log_ls,K=K):
    times = 0
    for log in log_ls:
        if log % min_length == 0:
            times += log // min_length -1
        else:
            times += log // min_length
    if times <= K:
        return True
    else:
        return False
#print(less_k(5,[10,10],2))

def return_min_length():
    r = Max
    l = -1
    while True:
        next_length = (r+l) // 2
        if next_length == 0 or not less_k(next_length):
            l = next_length
        else:
            r = next_length
        if r - l == 1:
            return r

ans = return_min_length()
print(ans)

