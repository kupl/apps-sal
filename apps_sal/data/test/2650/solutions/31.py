import sys
import bisect
import heapq

N_MAX = 2*10**5
A_MAX = 10**9

A = []
B = []
BB = [[] for _ in range(N_MAX)]

BBmax = []  # 各幼稚園の最大値

def max_rate_in_a_kg(kg):
    
    # 対象の幼稚園の最大レートを更新
    while BB[kg]:
        rate, k = BB[kg][0]
        if B[k] == kg:  # いるならOK
            return -rate
        else:
            heapq.heappop(BB[kg])  # 転園していれば削除

    return 0


def max_rate():
    while BBmax:
        rate, kg_no = BBmax[0]
        if max_rate_in_a_kg(kg_no) == rate:
            return rate
        else:
            heapq.heappop(BBmax)
    return None

def p():
    for i in range(len(BB)):
        if BB[i] != []:
            print(i, BB[i])

def pp():
    print("BBmax : ", end="")
    for i in range(len(BBmax)):
        print(BBmax[i], end=" ")
    print()


def main():

    N, Q = map(int, sys.stdin.readline().split())

    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        A.append(a)  # レート
        B.append(b-1)  # 幼稚園番号も0からにする
        heapq.heappush(BB[b-1],(-a,i))  # BB は最大が最も左に来るようにする

    for kg_no in range(N_MAX):
        rate = max_rate_in_a_kg(kg_no)
        if rate > 0:
            BBmax.append((rate, kg_no))
    heapq.heapify(BBmax)

    # p()
    # pp()

    for i in range(Q):
        # print("====")
        c, d = map(int, sys.stdin.readline().split())

        kid_no = c-1  # 園児番号
        after = d-1  # 幼稚園番号

        # 転出
        before = B[kid_no]
        B[kid_no] = after  # 園児の所属を更新

        heapq.heappush(BB[after], (-A[kid_no], kid_no))  # 幼稚園の最大を更新
        # p()

        new_rate_kg = max_rate_in_a_kg(before)  # 転入元の最大を更新
        if new_rate_kg != 0:
            heapq.heappush(BBmax, (new_rate_kg, before))

        new_rate_kg = max_rate_in_a_kg(after)  # 転園先の最大レートを更新
        if new_rate_kg != 0:
            heapq.heappush(BBmax, (new_rate_kg, after))  # BBmax を更新

        # pp()
        print(max_rate())

def __starting_point():
    main()
__starting_point()
