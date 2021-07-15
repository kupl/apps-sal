n = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))
A_list = sorted(A_list)
B_list = sorted(B_list)
C_list = sorted(C_list)
cnt = 0

def is_ok(arg): #　B　より小さい最大の　A
    return A_list[arg] < B_list[i]

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def is_ok2(arg): #　B　より大きい最小の　A
    return C_list[arg] > B_list[i]

def bisect2(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok2(mid):
            ok = mid
        else:
            ng = mid
    return ok

for i in range(n): #Bを固定
    #Bより小さいAを探す
    A_key = bisect(len(A_list), 0)
    if A_list[A_key] < B_list[i]:
        #Bより大きいCを探す
        C_key = bisect2(-1, len(C_list)-1)
        if B_list[i] < C_list[C_key]:
            #print(A_key, i, C_key, A_list[A_key], B_list[i], C_list[C_key])
            cnt += (n-C_key)*(A_key+1)

print(cnt)

