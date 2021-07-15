"""
1 ----- 2 ----- ai ----- bi -----
                    辺:i
"""
import itertools

def one_stroke_path():
    """
    N : 頂点
    M : 辺数
    ai, bi : 辺iの両端の頂点
    """
    # 入力
    N, M = list(map(int, input().split()))
    a = list()
    b = list()
    for _ in range(M):
        A, B = list(map(int, input().split()))
        a.append(A)
        b.append(B)
    
    # 処理
    permutations_list = itertools.permutations([x for x in range(1,N+1)])
    count = 0
    for one_case in permutations_list:
        is_ok = False
        if one_case[0] == 1:
            for i in range(len(one_case)-1):
                for j in range(M):
                    if (one_case[i] == a[j] and one_case[i+1] == b[j]) or (one_case[i] == b[j] and one_case[i+1] == a[j] ):
                        is_ok = True
                        break
                    else:
                        is_ok = False
                if is_ok == False:
                    break
        else:
            is_ok = False
        if is_ok:
            count += 1
    return count

result = one_stroke_path()
print(result)


