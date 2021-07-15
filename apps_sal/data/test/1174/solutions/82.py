import copy

def bi_search(money,M,N):
    money.sort()
    #list = []
    #for i in range(0,money[N-1]+2,1):
        #list.append(i)
    left = 0
    right = money[N-1]+1
    mid = 0
    #print(list,left,right)
    while True:
        mid = int( (left+right)/2 )
        cnt = 0
        #print(left,right,mid)
        #print(money)
        money_tmp = copy.copy(money)
        for i in range(N):
            while True:
                #print(money_tmp[i],i)
                if money_tmp[i] <= mid:
                    break
                else:
                    money_tmp[i] //= 2
                    cnt += 1
        #print(cnt)
        if cnt == M:
            return mid,cnt
        elif cnt < M:
            right = mid
            tmp = cnt
        elif cnt > M:
            left = mid + 1

        if left == right:
            return right,tmp

def main():
    N,M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    max_money,cnt = bi_search(A,M,N)
    #print (cnt)
    cnt = M-cnt
    ans = 0
    for i in range(N):
        if max_money >= A[i]:
            continue
            #ans += A[i]
        else:
            while True:
                A[i] //= 2
                if max_money >= A[i]:
                    #ans += A[i]
                    break
    A.sort(reverse = True)
    j = 0
    if A[j] == 0:
        return 0
    for i in range(cnt):
        A[j] //= 2
        j += 1

    for i in range(N):
        ans += A[i]

    return ans

print((main()))

